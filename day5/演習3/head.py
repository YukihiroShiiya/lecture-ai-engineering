import requests

# GitHubトークンをここに貼り付け（セキュアに管理してください）
token = "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"  # ご自身のPATに置き換えてください
owner = "YukihiroShiiya"
repo = "lecture-ai-engineering"

url = f"https://api.github.com/repos/{owner}/{repo}/branches"
headers = {
    "Authorization": f"token {token}",
    "Accept": "application/vnd.github+json"
}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    print("✅ 利用可能なブランチ一覧:")
    for branch in response.json():
        print("-", branch["name"])
else:
    print("❌ ブランチ一覧の取得に失敗:", response.status_code)
    print(response.text)