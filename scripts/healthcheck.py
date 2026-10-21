#!/usr/bin/env python3
"""健康检查 + 自愈。

流程:
  1. 构建（失败自动重试 N 次）
  2. 链接检查
  3. 线上地址检查（首页 + sitemap.xml 返回 200，带退避重试）
  失败处理:
  - 构建/链接检查仍失败 -> 回滚到"最后一次正常"的提交（git tag last-good，
    没有 tag 时自动向前找最近一个能构建通过的提交），恢复内容和配置后重新构建。
  - 全部通过 -> 把 last-good 标签移到当前提交。
  每次运行把结果写入 state/status.json（最新）和 state/status.jsonl（历史）。

用法:
  python scripts/healthcheck.py [--live] [--live-url URL] [--rollback] [--commit] [--mark-good]
退出码: 0 正常或已成功回滚(看 status.json 的 result); 1 构建/链接失败且无法自愈; 2 线上地址不可用
"""
import argparse
import datetime as dt
import json
import os
import shutil
import subprocess
import sys
import tempfile
import time
import urllib.request

from common import ROOT, STATE, load_site

PY = sys.executable
RESTORE_PATHS = ["content", "niches", "site.yaml", "templates", "static", "scripts"]
TAG = "last-good"


def sh(cmd, cwd=ROOT, check=False):
    r = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and r.returncode:
        raise RuntimeError(f"{' '.join(cmd)} failed: {r.stderr.strip()}")
    return r


def build_and_check(cwd=ROOT, retries=0, log=None):
    for attempt in range(retries + 1):
        b = sh([PY, "scripts/build.py"], cwd)
        if b.returncode == 0:
            l = sh([PY, "scripts/linkcheck.py"], cwd)
            if l.returncode == 0:
                if log is not None:
                    log.append(f"build+linkcheck OK (attempt {attempt + 1})")
                return True, b.stdout + l.stdout
            out = l.stdout + l.stderr
        else:
            out = b.stdout + b.stderr
        if log is not None:
            log.append(f"attempt {attempt + 1} failed: {out.strip()[-500:]}")
        time.sleep(min(2 ** attempt, 10) if attempt < retries else 0)
    return False, out


def is_git():
    return sh(["git", "rev-parse", "--is-inside-work-tree"]).returncode == 0


def candidates():
    c = []
    t = sh(["git", "rev-parse", "--verify", "-q", f"{TAG}^{{commit}}"])
    if t.returncode == 0:
        c.append(t.stdout.strip())
    revs = sh(["git", "rev-list", "-n", "10", "HEAD"]).stdout.split()
    head = revs[0] if revs else None
    c += [r for r in revs[1:] if r not in c]
    return [x for x in c if x != head] or ([head] if head and t.returncode == 0 else [])


def rollback(log, commit=False):
    if not is_git():
        log.append("rollback skipped: not a git repo")
        return None
    for sha in candidates():
        tmp = tempfile.mkdtemp(prefix="autosite-rb-")
        try:
            if sh(["git", "worktree", "add", "--detach", tmp, sha]).returncode:
                continue
            # 复用当前 venv 依赖，在旧提交上验证能否构建
            ok, _ = build_and_check(cwd=tmp)
            if ok:
                # 未提交的改动先 stash 保存（可用 git stash list 找回），绝不直接丢弃
                if sh(["git", "status", "--porcelain", "--"] + RESTORE_PATHS).stdout.strip():
                    sh(["git", "stash", "push", "-u", "-m", "autosite pre-rollback", "--"] + RESTORE_PATHS)
                    log.append("uncommitted changes stashed (git stash list)")
                # restore 会同时删除"好版本之后新增"的已跟踪文件
                sh(["git", "restore", f"--source={sha}", "--staged", "--worktree", "--"] + RESTORE_PATHS, check=True)
                log.append(f"rolled back working tree to {sha[:10]}")
                if commit:
                    sh(["git", "add", "-A", "--"] + RESTORE_PATHS)
                    c = sh(["git", "commit", "-qm", f"auto-rollback to {sha[:10]}"])
                    log.append("rollback committed" if c.returncode == 0 else "nothing to commit after rollback")
                return sha
            log.append(f"candidate {sha[:10]} also fails, trying older")
        finally:
            sh(["git", "worktree", "remove", "--force", tmp])
            shutil.rmtree(tmp, ignore_errors=True)
    log.append("no good commit found to roll back to")
    return None


def live_ok(url, retries, log):
    targets = [url.rstrip("/") + "/", url.rstrip("/") + "/sitemap.xml"]
    for attempt in range(retries):
        bad = []
        for t in targets:
            try:
                req = urllib.request.Request(t, headers={"User-Agent": "autosite-health/1.0", "Cache-Control": "no-cache"})
                with urllib.request.urlopen(req, timeout=20) as r:
                    if r.status != 200:
                        bad.append(f"{t} -> {r.status}")
            except Exception as e:  # noqa: BLE001
                bad.append(f"{t} -> {e}")
        if not bad:
            log.append(f"live OK: {', '.join(targets)} returned 200")
            return True
        log.append(f"live attempt {attempt + 1} failed: {bad}")
        if attempt < retries - 1:
            time.sleep(min(5 * 2 ** attempt, 60))
    return False


def write_status(status):
    STATE.mkdir(exist_ok=True)
    (STATE / "status.json").write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    with open(STATE / "status.jsonl", "a", encoding="utf-8") as f:
        f.write(json.dumps(status, ensure_ascii=False) + "\n")


def main():
    cfg = load_site()
    h = cfg.get("health", {})
    ap = argparse.ArgumentParser()
    ap.add_argument("--live", action="store_true", help="检查线上地址")
    ap.add_argument("--live-url", default=os.environ.get("LIVE_URL") or os.environ.get("SITE_BASE_URL") or cfg["site"]["base_url"])
    ap.add_argument("--rollback", action="store_true", help="构建失败时自动回滚")
    ap.add_argument("--commit", action="store_true", help="回滚后自动提交")
    ap.add_argument("--mark-good", action="store_true", help="通过后把 last-good 标签移到 HEAD")
    ap.add_argument("--live-only", action="store_true", help="只检查线上地址（部署后用）")
    a = ap.parse_args()

    log, status = [], {"time": dt.datetime.now(dt.timezone.utc).astimezone().isoformat(timespec="seconds")}
    if is_git():
        status["commit"] = sh(["git", "rev-parse", "--short", "HEAD"]).stdout.strip()

    if a.live_only:
        a.live, ok = True, True
        status["build"] = "skipped"
    else:
        ok, _ = build_and_check(retries=h.get("build_retries", 2), log=log)
        status["build"] = "ok" if ok else "fail"
    code = 0
    if not ok:
        code = 1
        if a.rollback:
            sha = rollback(log, commit=a.commit)
            status["rolled_back_to"] = sha
            if sha:
                ok2, _ = build_and_check(log=log)
                status["build_after_rollback"] = "ok" if ok2 else "fail"
                if ok2:
                    code = 0  # 已自愈：dist/ 是最后一个正常版本，可以继续部署
                    print("[health] WARNING: build failed, auto-rolled back to", sha[:10], file=sys.stderr)
    if a.live:
        live = live_ok(a.live_url, h.get("live_url_retries", 3), log)
        status["live"] = "ok" if live else "fail"
        if not live and code == 0:
            code = 2
    if code == 0 and a.mark_good and is_git() and not status.get("rolled_back_to"):
        sh(["git", "tag", "-f", TAG, "HEAD"])
        log.append(f"tag {TAG} -> HEAD")
    status["result"] = ("rolled_back" if status.get("rolled_back_to") and code == 0
                        else "healthy" if code == 0 else "unhealthy")
    status["log"] = log
    write_status(status)
    print(json.dumps(status, ensure_ascii=False, indent=2))
    return code


if __name__ == "__main__":
    sys.exit(main())
