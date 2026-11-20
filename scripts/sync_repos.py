#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
同步 zseagate 的仓库列表到 profile README（自动维护段）。

由 .github/workflows/sync-repos.yml 定时调用；也可本地手动运行（设置 GITHUB_TOKEN 可选）。

行为：读取 https://api.github.com/users/zseagate/repos，按创建时间倒序，
在 README.md 的 <!-- AUTO-SYNC:START --> / <!-- AUTO-SYNC:END --> 段内
生成“全部仓库”列表；NEW_DAYS 天内新建的仓库标记 🆕。
仅当内容变化时才写回 README.md（避免产生空提交）。
"""
import os
import re
import sys
import json
import datetime
import pathlib
import urllib.request
import urllib.error

OWNER = "zseagate"
PROFILE_REPO = "zseagate"   # profile 仓库自身，不列出
NEW_DAYS = 30               # 多少天内算“新增仓库”
README = pathlib.Path(__file__).resolve().parent.parent / "README.md"
START = "<!-- AUTO-SYNC:START -->"
END = "<!-- AUTO-SYNC:END -->"

API = f"https://api.github.com/users/{OWNER}/repos?per_page=100&sort=created&direction=desc"


def fetch_repos():
    token = os.environ.get("GITHUB_TOKEN") or os.environ.get("GH_TOKEN")
    headers = {"Accept": "application/vnd.github+json",
               "User-Agent": "zseagate-profile-sync",
               "X-GitHub-Api-Version": "2022-11-28"}
    if token:
        headers["Authorization"] = f"Bearer {token}"

    import time
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


def build_block(repos):
    now = datetime.datetime.now(datetime.timezone.utc)
    lines = [
        START,
        "## 🆕 仓库列表（自动同步）",
        "",
        "> 由 GitHub Actions 按创建时间倒序自动生成，每 24 小时更新；**🆕** = "
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
        desc = (repo.get("description") or "").strip()
        desc = re.sub(r"\s+", " ", desc)            # 折叠换行 / 多余空白
        desc = re.sub(r"^[\s\-–—:：|]+", "", desc)  # 去掉开头多余分隔符
        suffix = f" — {desc}" if desc else ""
        lines.append(f"- [{name}](https://github.com/{OWNER}/{name}){badge}{suffix} · {created}")
    lines += ["", END]
    return "\n".join(lines) + "\n"


def main():
    repos = fetch_repos()
    block = build_block(repos).rstrip("\n")
    readme = README.read_text(encoding="utf-8") if README.exists() else ""
    if START in readme and END in readme:
        pattern = re.compile(re.escape(START) + r".*?" + re.escape(END), re.DOTALL)
        updated, n = pattern.subn(block, readme, count=1)
    else:
        # 没有标记段时，追加到文件末尾（首次运行），避免多加多余空行
        sep = "" if readme.endswith("\n") else "\n"
        updated, n = (readme + sep + block), 1
    if n == 0:
        print("AUTO-SYNC markers not found; nothing written.", file=sys.stderr)
        return 1
    if updated != readme:
        README.parent.mkdir(parents=True, exist_ok=True)
        README.write_text(updated, encoding="utf-8")
        print("README.md updated.")
    else:
        print("README.md unchanged.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
