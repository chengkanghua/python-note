from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

KEY = "4E2918885FD98109869D14E0231A0BF4"
KEY = binascii.a2b_hex(KEY)

IV = "16B17E519DDD0CE5B79D7A63A4DD801C"
IV = binascii.a2b_hex(IV)


def aes_encrypt(data_string):
    aes = AES.new(
        key=KEY,
        mode=AES.MODE_CBC,
        iv=IV
    )
    raw = pad(data_string.encode('utf-8'), 16)
    aes_bytes = aes.encrypt(raw)
    return binascii.b2a_hex(aes_bytes).decode().upper()


data = "|20445933|n000094fgki|1631632032|mg3c3b04ba|1.3.5|ktk3s1js_xw0ljnwa6j|4330701|https://w.yangshipin.cn/|mozilla/5.0 (macintosh; ||Mozilla|Netscape|MacIntel|"
result = aes_encrypt(data)
print(f"--01{result}")
