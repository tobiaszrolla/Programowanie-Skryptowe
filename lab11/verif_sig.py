from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256

with open("public.pem", "rb") as f:
    public_key = RSA.import_key(f.read())

with open("./lab11/file.txt", "rb") as f:
    data = f.read()

with open("./plik.txt.sig", "rb") as f:
    signature = f.read()

h = SHA256.new(data)

pkcs1_15.new(public_key).verify(h, signature)

print("OK — podpis poprawny")