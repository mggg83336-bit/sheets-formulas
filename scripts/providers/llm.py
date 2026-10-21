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
