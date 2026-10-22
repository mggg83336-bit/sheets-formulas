#!/usr/bin/env bash
# 每日例行（本机/服务器 cron 版；GitHub Actions 版见 .github/workflows/deploy.yml）
# update -> build -> health check(失败自动回滚) -> push(触发 Pages 部署) -> 线上检查
set -uo pipefail
cd "$(dirname "$0")/.."
PY="${PY:-$( [ -x .venv/bin/python ] && echo .venv/bin/python || echo python3 )}"

"$PY" scripts/generate.py                                         # 1. 生成新内容
git add content niches && git commit -qm "auto: content $(date +%F)" || true
"$PY" scripts/healthcheck.py --rollback --commit --mark-good       # 2. 构建+链接检查，失败回滚
rc=$?
if [ "${AUTOSITE_PUSH:-0}" = "1" ] && git remote get-url origin >/dev/null 2>&1; then
  git push -q origin HEAD && git push -qf origin last-good || echo "push failed"   # 3. 部署
  sleep "${DEPLOY_WAIT:-120}"
  "$PY" scripts/healthcheck.py --live-only || rc=$?                 # 4. 线上 200 检查
fi
exit $rc
