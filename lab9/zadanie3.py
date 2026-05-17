import requests
import sys

IP_adress = sys.argv[1]

response = requests.get(f"https://internetdb.shodan.io/{IP_adress}")

if response.status_code == 200:
    data = response.json()
    ports = data["ports"]
    hostnames = data["hostnames"]
    print("Adres IP: ",IP_adress)
    print("Hostname: ",hostnames)
    print("Porty: ",ports)
else:
    print("Błąd: ",response.status_code)