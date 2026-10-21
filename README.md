# autosite —— 全自动静态内容站底座

选定方向后，只需改 `site.yaml` 和 `niches/<方向>/`，之后每天由 GitHub Actions 自动完成
**生成内容 → 构建 → 部署 → 健康检查 / 自愈**，日常不需要任何人工操作。

## 目录结构

```
autosite/
├── site.yaml                  # 全站唯一配置：站名、网址、方向、广告代码、商品/联盟链接、健康检查参数
├── niches/example/            # 方向配置（换方向就复制这个目录）
│   ├── niche.yaml             #   关键词/主题列表 + 标题/摘要/正文模板（Jinja2）
│   └── items.csv              #   可选结构化数据，每行生成一页（程序化 SEO）
├── content/posts/*.md         # 生成出来的文章（带 front matter，会提交进仓库）
├── templates/                 # 页面模板：base/index/post/404，广告位 _ad.html，购买按钮 _products.html
├── static/style.css
├── scripts/
│   ├── generate.py            # 内容流水线（幂等：已写过的关键词自动跳过）
│   ├── providers/             # 内容生成器插槽：template（默认免费）/ llm（大模型预留位）
│   ├── build.py               # 构建 dist/：页面 + sitemap.xml + robots.txt + feed.xml(RSS) + 404
│   ├── linkcheck.py           # 链接检查（站内必查，站外可选）
│   ├── healthcheck.py         # 健康检查 + 重试 + 回滚 + 状态日志
│   └── daily.sh               # 不用 GitHub Actions 时的本机 cron 版每日例行
├── .github/workflows/deploy.yml  # push 和每日定时：生成→构建→自愈→部署 Pages→线上检查
└── state/status.json(l)       # 健康检查结果（最新一次 / 历史），已 gitignore
```

## 本地运行

```bash
python3 -m venv .venv && .venv/bin/pip install -r requirements.txt
.venv/bin/python scripts/generate.py           # 生成新文章（数量由 generate_per_run 控制）
.venv/bin/python scripts/build.py              # 构建到 dist/
.venv/bin/python scripts/linkcheck.py          # 检查链接（加 --external 检查站外）
.venv/bin/python scripts/healthcheck.py --rollback --mark-good   # 构建+检查，失败自动回滚
SITE_BASE_URL=http://127.0.0.1:8765 .venv/bin/python scripts/build.py && \
  python3 -m http.server 8765 --directory dist   # 本地预览
```

## 换方向（接入具体业务）

1. 复制 `niches/example` 为 `niches/<新方向>`，改 `topics` 关键词列表、模板，或者放一个 CSV。
2. 在 `site.yaml` 里改 `niche`、站名、`base_url`，把广告代码粘到 `ads`，把 Gumroad / Lemon Squeezy
   的商品链接填进 `products`，联盟链接填进 `affiliate_links`。
   广告和商品在**构建时**插入，改配置后所有旧文章会同步更新。
3. 想用大模型写正文：在 `scripts/providers/llm.py` 接入（目前是占位，默认不调用任何付费接口），
   把 `site.yaml` 的 `provider` 改成 `llm`，在仓库 Secrets 配 `LLM_API_URL` / `LLM_API_KEY`。
   调用失败会自动退回模板生成，不会让定时任务中断。

## 每日自动流程（GitHub Actions：`.github/workflows/deploy.yml`）

每天 UTC 01:17（北京时间 09:17）自动运行，平时 push 也会触发：

1. **更新**：`generate.py` 生成当天新文章，自动提交进仓库。
2. **构建**：`healthcheck.py` 调用 `build.py`，失败会自动重试（次数见 `health.build_retries`）。
3. **检查 + 自愈**：`linkcheck.py` 检查所有站内链接，以及 sitemap/robots/RSS/404 是否都在。
   还是失败的话，自动回滚到最近一次正常的提交（`last-good` 标签；没有标签就往前逐个试最近 10 个提交），
   提交一个 `auto-rollback` 再重新构建，保证线上始终是能用的版本。
   全部通过后，`last-good` 标签移到当前提交。
4. **部署**：把 `dist/` 发布到 GitHub Pages。
5. **线上检查**：首页和 sitemap.xml 必须返回 200，失败会退避重试；仍然失败就自动重新部署一次。
6. **日志**：每次的结果都写进 `state/status.json`，也作为 Actions 产物保存，可以随时查看。

> 用 GitHub Token 推送的自动提交不会再次触发工作流，不会形成死循环。

不用 GitHub Actions 的话，可以在任意 Linux 机器上配 cron：
`9 9 * * * cd /path/autosite && AUTOSITE_PUSH=1 ./scripts/daily.sh >> state/cron.log 2>&1`

## 可选：Cloudflare Pages

Cloudflare Pages → Create project → 连接这个 GitHub 仓库。
构建命令填 `pip install -r requirements.txt && python scripts/generate.py --limit 0 && python scripts/build.py`，
输出目录填 `dist`，环境变量 `SITE_BASE_URL` 设为 Cloudflare 分配的域名（或自定义域名）。
每日更新仍然由 GitHub Actions 的定时任务负责（它会提交新内容，Cloudflare 检测到推送就自动重新构建）。
这种情况下可以删掉 workflow 里的 `deploy` 任务，`live-check` 的 `LIVE_URL` 改成 Cloudflare 的域名。

## ⚠️ 必须由老板本人做一次的事（之后都不用再管）

| # | 步骤 | 说明 |
|---|------|------|
| 1 | **GitHub 账号** | 注册或登录 GitHub，新建一个仓库（公开仓库可以免费用 Pages），把本目录推上去；或者在自己的 1 对 1 对话里给执行官授权 GitHub 连接，由执行官来推。 |
| 2 | **开启 Pages** | 仓库 Settings → Pages → Source 选 **GitHub Actions**。 |
| 3 | **Actions 权限** | Settings → Actions → General → Workflow permissions 选 **Read and write**（自动提交内容、回滚、打标签都要用）。 |
| 4 | **填写网址** | 把 `site.yaml` 的 `base_url` 改成 `https://<用户名>.github.io/<仓库名>`（CI 会自动识别，这一步主要影响本地构建）。 |
| 5 | **广告联盟实名**（可选） | 申请 Google AdSense 之类的广告联盟，需要本人实名、绑定收款账户、验证网站所有权，审核通过后把代码粘进 `site.yaml → ads`。 |
| 6 | **商品/收款平台实名**（可选） | 开通 Gumroad / Lemon Squeezy 店铺，完成身份和收款信息（银行卡/PayPal 等）验证，上架商品后把链接填进 `products`。 |
| 7 | **联盟计划**（可选） | 注册联盟推广计划（实名、税务信息），把带推广码的链接填进 `affiliate_links`。 |
| 8 | **搜索引擎收录**（可选，推荐） | 在 Google Search Console / Bing Webmaster 验证网站，提交 `sitemap.xml`。 |
| 9 | **大模型 Key**（可选） | 用 `llm` 生成器时，在仓库 Secrets 填 `LLM_API_URL` / `LLM_API_KEY`。 |

以上做完之后，日常不需要任何人工操作。
