from Crypto.Cipher import AES
from Crypto.Util.Padding import pad


def aes_encrypt(data_string):
    key = "fd6b639dbcff0c2a1b03b389ec763c4b"
    iv = "77b07a672d57d64c"
    aes = AES.new(
        key=key.encode('utf-8'),
        mode=AES.MODE_CBC,
        iv=iv.encode('utf-8')
    )
    raw = pad(data_string.encode('utf-8'), 16)
    return aes.encrypt(raw)


data = "aadzfalskdjf;lkaj;dkjfa;skdjf;akjsdf;kasd;fjaoqwierijhnlakjdhf"
result = aes_encrypt(data)
print(result)
