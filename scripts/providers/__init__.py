"""内容生成器插槽。

每个 provider 实现一个函数：
    generate(topic: dict, niche: dict, ctx: dict) -> dict
返回 {"title": str, "summary": str, "tags": [str], "body_md": str}

- template: 默认，零成本，按 niche.yaml 里的模板渲染。
- llm:      预留接入大模型的位置（见 llm.py），失败时自动回落到 template。
"""
from . import template, llm

PROVIDERS = {"template": template.generate, "llm": llm.generate}


def get_provider(name: str):
    if name not in PROVIDERS:
        raise ValueError(f"unknown provider: {name}; choose from {list(PROVIDERS)}")
    return PROVIDERS[name]
