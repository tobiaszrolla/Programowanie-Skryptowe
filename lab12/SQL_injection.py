import requests

payloads = ["1", "'", '"']

for payload in payloads:
    r = requests.get(
        "http://localhost/DVWA/vulnerabilities/sqli/",
        params={"id": payload}
    )

    print(payload, r.status_code)