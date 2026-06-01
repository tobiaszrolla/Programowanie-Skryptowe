import sys
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

path = sys.argv[1]
key = get_random_bytes(16)

try: 
    with open(path, "rb") as file:
        data = file.read()
except:
   print("Canot open file")
   sys.exit(1)

cipher = AES.new(key, AES.MODE_EAX)
nonce = cipher.nonce
ciphertext, tag = cipher.encrypt_and_digest(data)
print("KEY:")
print(key)
try:
    with open(path, "wb") as file:
        file.write(ciphertext)
except:
    print("canot write to file")
    sys.exit(1)