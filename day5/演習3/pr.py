import requests
import os

token = os.environ.get("github_token")
owner = "YukihiroShiiya"
repo = "lecture-ai-engineering"
head_branch = "develop"
base_branch = "master"
title = "✨ 新機能の追加"
body = "このPRでは新機能を追加しました。レビューをお願いします。"

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

if response.status_code == 201:
    pr_url = response.json()["html_url"]
    print(f"✅ PR 作成成功: {pr_url}")
else:
    print(f"❌ PR 作成失敗: {response.status_code}")
    print(response.text)
