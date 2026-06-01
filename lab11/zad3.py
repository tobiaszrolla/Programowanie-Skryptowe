from Crypto.PublicKey import RSA
from Crypto.Signature import pkcs1_15
from Crypto.Hash import SHA256
import sys

try:
    with open("private.pem", "rb") as f:
        private_key = RSA.import_key(f.read())
except:
    print("cannot get key")
    sys.exit(1)
    
path = sys.argv[1]

try: 
    with open(path, "rb") as file:
        data = file.read()
except:
   print("Canot open file")
   sys.exit(1)

hash = SHA256.new(data)
signature = pkcs1_15.new(private_key).sign(hash)
with open("plik.txt.sig", "wb") as f:
    f.write(signature)


