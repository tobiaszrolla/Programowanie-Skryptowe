import requests
import sys
url = sys.argv[1]

payloads = [
    "'"
    "''"
    "')"
]

sql_errors = [
    "sql syntax",
    "mysql",
    "postgresql",
    "ora-",
    "sqlite"
]

for payload in payloads:

    try:
        response = requests.get(
            url,
            params={"id": payload},
            timeout=5
        )

        content = response.text.lower()

        for error in sql_errors:
            if error in content:
                print(
                    f"[!] Możliwa podatność SQL Injection\n"
                    f"Payload: {payload}\n"
                    f"Błąd: {error}\n"
                )

    except Exception as e:
        print(f"Błąd połączenia: {e}")