"""共享工具：读配置、读写带 front matter 的 Markdown。"""
import re
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
CONTENT = ROOT / "content" / "posts"
DIST = ROOT / "dist"
STATE = ROOT / "state"

# 占位符：内容里只写占位符，构建时再替换成 site.yaml 里的最新广告/商品代码，
# 这样改配置后旧文章也会同步更新。
AD_PLACEHOLDER = "<!--AD_IN_ARTICLE-->"
PRODUCT_PLACEHOLDER = "<!--PRODUCT_BOX-->"


def load_site():
    return yaml.safe_load((ROOT / "site.yaml").read_text(encoding="utf-8"))


def load_niche(name):
    d = ROOT / "niches" / name
    n = yaml.safe_load((d / "niche.yaml").read_text(encoding="utf-8"))
    n["_dir"] = d
    return n


def slugify(s: str) -> str:
    s = s.strip().lower()
    s = re.sub(r"[^\w\u4e00-\u9fff-]+", "-", s)
    return re.sub(r"-+", "-", s).strip("-") or "post"


def read_post(path: Path):
    text = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    if not m:
        raise ValueError(f"{path}: missing front matter")
    meta = yaml.safe_load(m.group(1)) or {}
    for k in ("title", "date", "slug"):
        if k not in meta:
            raise ValueError(f"{path}: front matter missing '{k}'")
    return meta, m.group(2)


def write_post(path: Path, meta: dict, body: str):
    fm = yaml.safe_dump(meta, allow_unicode=True, sort_keys=False).strip()
    path.write_text(f"---\n{fm}\n---\n{body.strip()}\n", encoding="utf-8")
