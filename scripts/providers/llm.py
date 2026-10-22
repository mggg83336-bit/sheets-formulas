"""大模型生成器 —— 插槽（STUB）。

这里是接入 LLM 的唯一位置。默认不调用任何付费 API：
- 未设置环境变量 LLM_API_URL 时，直接回落到 template 生成器。
- 设置后，按 OpenAI 兼容的 /chat/completions 接口调用（可指向本地 Ollama 等免费服务）：
    LLM_API_URL=http://localhost:11434/v1/chat/completions
    LLM_MODEL=qwen2.5
    LLM_API_KEY=（可选；在 GitHub Actions 中放到 Secrets，切勿写进仓库）
任何异常都会回落到 template，保证定时任务不中断。
"""
import json
import os
import urllib.request

from . import template

PROMPT = (
    "你是{niche}领域的编辑。围绕关键词「{kw}」写一篇 600 字左右的中文实用文章，"
    "使用 Markdown 二级标题，事实要谨慎、不夸大。补充信息：{data}"
)


def generate(topic: dict, niche: dict, ctx: dict) -> dict:
    base = template.generate(topic, niche, ctx)  # 标题/摘要/标签沿用模板
    url = os.environ.get("LLM_API_URL")
    if not url:
        return base
    try:
        payload = {
            "model": os.environ.get("LLM_MODEL", "default"),
            "messages": [{"role": "user", "content": PROMPT.format(
                niche=niche.get("name", ""), kw=topic["keyword"],
                data=json.dumps(topic.get("data", {}), ensure_ascii=False))}],
        }
        req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={
            "Content-Type": "application/json",
            **({"Authorization": f"Bearer {os.environ['LLM_API_KEY']}"} if os.environ.get("LLM_API_KEY") else {}),
        })
        with urllib.request.urlopen(req, timeout=120) as r:
            text = json.load(r)["choices"][0]["message"]["content"].strip()
        if len(text) < 200:
            raise ValueError("LLM output too short")
        base["body_md"] = text + "\n\n" + ctx.get("product_box", "")
    except Exception as e:  # noqa: BLE001 —— 任何失败都回落，保证无人值守
        print(f"[llm] fallback to template: {e}")
    return base


# ---------------------------------------------------------------- structured niches
ENTRY_PROMPT = """You write one page for an Excel & Google Sheets formula help site.
Keyword: "{kw}" (platform: {platform}).
Return ONLY a JSON object with exactly the same keys and structure as this example entry
(different topic, same depth), no markdown fences:
{example}
Rules:
- Formulas must be correct, tested syntax for {platform}; note real differences between Excel and Google Sheets.
- The worked example must be small real data in "grid" (row 1 = headers). Every check gives the
  exact cell, formula and the exact result that formula returns on that grid (it will be recalculated
  and the page is rejected if any result is wrong).
- No filler, no marketing language. If the keyword is not a real, answerable spreadsheet task,
  return {{"skip": "reason"}}.
"""


def generate_entry(keyword, platform_key, slug, category, example_entry):
    """Ask an LLM (if configured) for a structured entry. Returns dict or None.

    The caller still runs the quality gate AND recalculates every example with LibreOffice
    before anything is published, so a wrong or thin answer is rejected, not posted.
    """
    url = os.environ.get("LLM_API_URL")
    if not url:
        return None
    ex = {k: v for k, v in example_entry.items() if not k.startswith("_") and k not in ("launch", "slugs", "related")}
    platform = "Excel" if platform_key == "excel" else "Google Sheets"
    payload = {
        "model": os.environ.get("LLM_MODEL", "default"),
        "messages": [{"role": "user", "content": ENTRY_PROMPT.format(
            kw=keyword, platform=platform, example=json.dumps(ex, ensure_ascii=False, default=str))}],
    }
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode(), headers={
            "Content-Type": "application/json",
            **({"Authorization": f"Bearer {os.environ['LLM_API_KEY']}"} if os.environ.get("LLM_API_KEY") else {}),
        })
        with urllib.request.urlopen(req, timeout=180) as r:
            text = json.load(r)["choices"][0]["message"]["content"].strip()
        text = text.removeprefix("```json").removeprefix("```").removesuffix("```").strip()
        entry = json.loads(text)
    except Exception as e:  # noqa: BLE001
        print(f"[llm] entry generation failed for {slug}: {e}")
        return None
    if not isinstance(entry, dict) or entry.get("skip"):
        print(f"[llm] skipped {slug}: {entry.get('skip') if isinstance(entry, dict) else 'bad output'}")
        return None
    entry.update({"id": slug, "slugs": {platform_key: slug}, "primary": platform_key,
                  "category": category or entry.get("category", "other"), "launch": False,
                  "related": [], "source": "llm"})
    return entry
