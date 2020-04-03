import hashlib

data = input()
output = hashlib.sha256(data.encode('utf-8'))
print(output.hexdigest())

