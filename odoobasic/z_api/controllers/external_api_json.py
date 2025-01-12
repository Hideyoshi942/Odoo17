import requests
import json

# Kết nối thông tin cơ bản
url = "http://127.0.0.1:8069"
db = "demo"
username = "admin"
password = "1"

# URL JSON-RPC endpoint
common_url = f"{url}/jsonrpc"
object_url = f"{url}/jsonrpc"

# Xác thực để lấy UID
payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "db": db,
        "login": username,
        "password": password,
    },
    "id": 1,
}

response = requests.post(f"{url}/web/session/authenticate", json=payload)
uid = response.json()["result"]["uid"]
if not uid:
    print("Authentication failed")
    exit()

# Trích xuất dữ liệu từ res.partner
payload = {
    "jsonrpc": "2.0",
    "method": "call",
    "params": {
        "model": "res.partner",
        "method": "search_read",
        "args": [],
        "kwargs": {
            "domain": [["is_company", "=", True]],
            "fields": ["name", "email"],
            "limit": 5,
        },
    },
    "id": 2,
}
response = requests.post(object_url, json=payload)
partners = response.json()["result"]

# In kết quả
print("Partners:", partners)
