#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
同步 zseagate 的仓库列表到 profile README（自动维护段）。

由 .github/workflows/sync-repos.yml 每日调用；也可本地手动运行（设置 GITHUB_TOKEN 可选）。

维护两段内容：
1. <!-- AUTO-SYNC:START/END -->  —— 全部仓库列表，创建时间倒序，30 天内标 🆕。
2. <!-- INDEX:START/END -->       —— 整个「项目索引」表格，分类与中文描述来自
                                      scripts/repos_meta.json（手工维护），
                                      未归类仓库自动进「🆕 新仓库（待归类）」段。

仅当内容变化时才写回 README.md（避免产生空提交）。
"""
import os
import re
import sys
import json
import time
import datetime
import pathlib
import urllib.request
import urllib.error

OWNER = "zseagate"
PROFILE_REPO = "zseagate"   # profile 仓库自身，不列出
NEW_DAYS = 30               # 多少天内算“新增仓库”

SCRIPTS = pathlib.Path(__file__).resolve().parent
README = SCRIPTS.parent / "README.md"
META = SCRIPTS / "repos_meta.json"

START = "<!-- AUTO-SYNC:START -->"
END = "<!-- AUTO-SYNC:END -->"
INDEX_START = "<!-- INDEX:START -->"
INDEX_END = "<!-- INDEX:END -->"

API = f"https://api.github.com/users/{OWNER}/repos?per_page=100&sort=created&direction=desc"


def fetch_repos():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    headers = {"Accept": "application/vnd.github+json",
               "User-Agent": "zseagate-profile-sync",
               "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    last_err = None
    for attempt in range(30):            # 网络偶发抖动，重试
        req = urllib.request.Request(API, headers=headers)
        try:
            with urllib.request.urlopen(req, timeout=60) as resp:
                return json.load(resp)
        except urllib.error.HTTPError as e:
            if e.code in (429, 403) and "rate limit" in (e.read(200).decode("utf-8", "ignore").lower()):
                last_err = f"rate limit ({e.code})"
            elif 500 <= e.code < 600:
                last_err = f"http {e.code}"
            else:
                raise
        except (urllib.error.URLError, OSError) as e:
            last_err = str(e)
        time.sleep(3)
    raise RuntimeError(f"failed to fetch repos after retries: {last_err}")


def github_desc(repo):
    """GitHub description 兜底：折叠空白、去开头分隔符、限长。"""
    d = (repo.get("description") or "（暂无描述）").strip()
    d = re.sub(r"\s+", " ", d)
    d = re.sub(r"^[\s\-–—:：|]+", "", d)
    if len(d) > 100:
        d = d[:99] + "…"
    return d


def table_desc(text):
    """Markdown 表格单元格内的描述：转义竖线。"""
    return re.sub(r"(?<!\\)\|", "\\|", (text or "").strip())


def build_block(repos):
    now = datetime.datetime.now(datetime.timezone.utc)
    lines = [
        START,
        "## 🆕 仓库列表（自动同步）",
        "",
        "> 由 GitHub Actions 按创建时间倒序自动生成，每日更新一次；**🆕** = "
        f"{NEW_DAYS} 天内新建的仓库。请勿手动编辑本段，改动会被覆盖。",
        f"> 最后更新：{now:%Y-%m-%d %H:%M} UTC",
        "",
    ]
    for repo in repos:
        name = repo["name"]
        if name == PROFILE_REPO:
            continue
        created_raw = repo["created_at"]
        created = created_raw[:10]
        created_dt = datetime.datetime.fromisoformat(created_raw.replace("Z", "+00:00"))
        badge = " 🆕" if (now - created_dt).days <= NEW_DAYS else ""
        desc = github_desc(repo)
        suffix = f" — {desc}" if desc else ""
        lines.append(f"- [{name}](https://github.com/{OWNER}/{name}){badge}{suffix} · {created}")
    lines += ["", END]
    return "\n".join(lines) + "\n"


def build_index_block(repos, meta):
    by_name = {r["name"]: r for r in repos}
    descriptions = meta.get("descriptions", {})
    groups = []
    seen = set()

    for cat in meta.get("categories", []):
        entries = []
        for name in cat.get("repos", []):
            if name in seen:
                continue
            seen.add(name)
            if name not in by_name:        # 已删除/改名的仓库跳过
                continue
            desc = descriptions.get(name) or github_desc(by_name[name])
            entries.append((name, desc))
        groups.append((cat.get("title", ""), entries))

    # GitHub 上有、元数据未归类的仓库 -> 新仓库段（创建时间倒序）
    extras = []
    for r in repos:
        name = r["name"]
        if name == PROFILE_REPO or name in seen:
            continue
        extras.append((name, github_desc(r), r.get("created_at", "")))
    extras.sort(key=lambda x: x[2], reverse=True)
    if extras:
        groups.insert(0, (meta.get("new_category_title", "🆕 新仓库（待归类）"),
                          [(n, d) for n, d, _ in extras]))

    lines = [INDEX_START]
    for title, entries in groups:
        if title:
            lines.append(f"### {title}")
        lines += ["| 项目 | 说明 |", "|---|---|"]
        for name, desc in entries:
            lines.append(f"| [{name}](https://github.com/{OWNER}/{name}) | {table_desc(desc)} |")
        lines.append("")
    if lines and lines[-1] == "":
        lines.pop()
    lines.append(INDEX_END)
    return "\n".join(lines) + "\n"


def replace_marker(text, start, end, block):
    block = block.rstrip("\n")
    if start in text and end in text:
        pattern = re.compile(re.escape(start) + r".*?" + re.escape(end), re.DOTALL)
        return pattern.sub(lambda m: block, text, count=1)
    # 没有标记段时追加到文件末尾（首次运行）
    sep = "" if text.endswith("\n") else "\n"
    return text + sep + block


def main():
    repos = fetch_repos()
    readme = README.read_text(encoding="utf-8") if README.exists() else ""

    updated = replace_marker(readme, START, END, build_block(repos))

    if META.exists():
        meta = json.loads(META.read_text(encoding="utf-8"))
        updated = replace_marker(updated, INDEX_START, INDEX_END, build_index_block(repos, meta))
    else:
        print("repos_meta.json missing; index block left unchanged", file=sys.stderr)

    if updated != readme:
        README.write_text(updated, encoding="utf-8")
        print("README.md updated.")
    else:
        print("README.md unchanged.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
