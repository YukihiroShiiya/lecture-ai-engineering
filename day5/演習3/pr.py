import requests
import os

#  認証情報 ---
token = os.environ["github_token"]  # ご自身のPATに置き換えてください
owner = "YukihiroShiiya"
repo = "lecture-ai-engineering"

# --- PR情報 ---
head_branch = "master"  # 作業ブランチ名（自分のブランチ）
base_branch = "master"                 # マージ先（通常は main や develop）
title = "✨ 新機能の追加"
body = "このPRでは新機能を追加しました。レビューをお願いします。"

# ---b API呼び出し ---
url = f"https://api.github.com/repos/{owner}/{repo}/pulls"
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json",
}
payload = {
    "title": title,
    "head": head_branch,
    "base": base_branch,
    "body": body,
}

response = requests.post(url, headers=headers, json=payload)

# --- 結果表示 ---
if response.status_code == 201:
    pr_url = response.json()["html_url"]
    print(f"✅ PR 作成成功: {pr_url}")
else:
    print(f"❌ PR 作成失敗: {response.status_code}")
    print(response.text)