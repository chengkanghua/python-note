# coding=utf-8
from Crypto.Cipher import AES
import json
import types
from firefly.utils.singleton import Singleton


class AesEncoder:
    __metaclass__ = Singleton

    NONE_TYPE = 0
    AES_TYPE = 1

    def __init__(self, password='@ZYHD#GDMJ!112233!love**foreverX', encode_type=1):
        self.aes_obj = AES.new(password, mode=AES.MODE_CFB)
        self.encode_type = encode_type

    def encode(self, msg):
        print "encode msg:", msg, self.encode_type
        if self.encode_type == self.NONE_TYPE:
            return msg
        elif self.encode_type == self.AES_TYPE:
            return self.encode_aes(msg)

    def encode_aes(self, msg):
        msg = self.byte_pad(msg)
        return self.aes_obj.encrypt(msg)

    def decode_aes(self, msg):
        try:
            decode_msg = self.byte_unpad(self.aes_obj.decrypt(msg))
        except Exception, e:
            return None

        msg_len = len(decode_msg)
        if msg_len == 0:
            return decode_msg

        try:
            json.loads(decode_msg)
        except ValueError:
            return None
        return decode_msg

    def decode(self, msg):
        if self.encode_type == self.NONE_TYPE:
            return msg
        elif self.encode_type == self.AES_TYPE:
            return self.decode_aes(msg)

    def byte_pad(self, text, byteAlignLen=16):
        count = len(text)
        mod_num = count % byteAlignLen
        if mod_num == 0:
            return text
        add_num = byteAlignLen - mod_num
        return text + chr(add_num) * add_num

    def byte_unpad(self, text, byteAlignLen=16):
        count = len(text)
        mod_num = count % byteAlignLen
        assert mod_num == 0
        lastChar = text[-1]
        lastLen = ord(lastChar)
        lastChunk = text[-lastLen:]
        if lastChunk == chr(lastLen) * lastLen:
            return text[:-lastLen]
        return text


if __name__ == '__main__':
    encoder = AesEncoder()
    from hashlib import md5
    print md5(encoder.encode_aes('test')).hexdigest()
