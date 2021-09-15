import hashlib

pwd = hashlib.sha256('123'.encode('utf-8')).hexdigest()
print(pwd)