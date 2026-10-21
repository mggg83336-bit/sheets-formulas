"""默认生成器：用 niche.yaml 中的 Jinja2 模板 + 结构化数据渲染 Markdown。"""
from jinja2 import Environment, StrictUndefined

_env = Environment(undefined=StrictUndefined, autoescape=False)


def _r(tpl: str, **v) -> str:
    return _env.from_string(tpl).render(**v).strip()


def generate(topic: dict, niche: dict, ctx: dict) -> dict:
    v = dict(keyword=topic["keyword"], data=topic.get("data", {}), niche=niche, **ctx)
    return {
        "title": _r(niche["title_template"], **v),
        "summary": _r(niche.get("summary_template", ""), **v),
        "tags": [_r(t, **v) for t in niche.get("tags_template", [])],
        "body_md": _r(niche["body_template"], **v),
    }
