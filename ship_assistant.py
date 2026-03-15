import requests
import gspread
from datetime import datetime
from oauth2client.service_account import ServiceAccountCredentials

# Google Sheet 設定
SHEET_URL = "https://docs.google.com/spreadsheets/d/1GJo4IYQmYPpStkHRZfXFLZnG-XgplLlL8PT09yDiE-Y"

scope = [
    "https://spreadsheets.google.com/feeds",
    "https://www.googleapis.com/auth/drive",
]

creds = ServiceAccountCredentials.from_json_keyfile_name(
    "google_credentials.json", scope
)
client = gspread.authorize(creds)

sheet = client.open_by_url(SHEET_URL).worksheet("Tracking")

rows = sheet.get_all_records()

for i, row in enumerate(rows, start=2):

    container = row["Container"]

    if not container:
        continue

    print(f"Checking {container}")

    # 模擬查詢 (之後會換成船公司查詢)
    eta = "2026-03-30"
    event = "Loaded Singapore"

    sheet.update(f"K{i}", eta)
    sheet.update(f"L{i}", event)
    sheet.update(f"N{i}", datetime.now().strftime("%Y-%m-%d %H:%M"))
