
from pathlib import Path
import os
import re

# 桃園藝文店設定
STORE_CODE = "TYYW"
STORE_NAME = "桃園藝文店"

# 自動抓取 YYYY-MM 格式的月份資料夾
pattern = re.compile(r"^\d{4}-\d{2}$")

folders = sorted([
    f for f in os.listdir()
    if pattern.match(f) and os.path.isdir(f)
])

def format_title(folder):
    return f"🦍🌍 WorldGym {STORE_CODE} 每日開發地圖 {folder} 💰"

html_head = '''<!DOCTYPE html>
<html lang="zh-Hant">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>WorldGym TYYW 地圖首頁</title>
    <style>
        body {
            font-family: "Segoe UI", sans-serif;
            padding: 40px;
        }
        h1 {
            font-size: 26px;
        }
        ul {
            list-style-type: none;
            padding-left: 0;
        }
        li {
            margin: 10px 0;
        }
        a {
            text-decoration: none;
            color: #1a73e8;
            font-size: 18px;
        }
        a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <h1>🦍🌍 WorldGym TYYW 地圖首頁</h1>
    <h2>桃園藝文店</h2>
    <ul>
'''

html_body = ""

for folder in folders:
    title = format_title(folder)
    html_body += f'        <li><a href="{folder}/index.html">{title}</a></li>\n'

html_tail = '''    </ul>
</body>
</html>
'''

full_html = html_head + html_body + html_tail

Path("index.html").write_text(
    full_html,
    encoding="utf-8"
)

print("✅ 已產生桃園藝文店首頁 index.html")
