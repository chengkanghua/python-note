import hashlib

def encrypt(data):
    hash_object = hashlib.md5()
    hash_object.update(data.encode('utf-8'))
    return hash_object.hexdigest()

v1 = encrypt('aaaaaa')
print(v1)