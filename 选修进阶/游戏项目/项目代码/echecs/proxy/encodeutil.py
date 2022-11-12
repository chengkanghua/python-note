# coding=utf-8

"""

"""

from Crypto.Cipher import AES
from firefly.utils.singleton import Singleton

import json

BS = AES.block_size
pad = lambda s: s + (BS - len(s) % BS) * chr(BS - len(s) % BS)
unpad = lambda s : s[0:-ord(s[-1])]


class AesEncoder:
    __metaclass__ = Singleton

    NONE_TYPE = 0
    AES_TYPE = 1

    def __init__(self, password='@ZYHD#GDMJ!112233!love**foreverX', encode_type=0):
        self.aes_obj = AES.new(password, mode=AES.MODE_CFB)
        self.encode_type = encode_type

    def encode(self, msg):
        if self.encode_type == self.NONE_TYPE:
            return msg
        elif self.encode_type == self.AES_TYPE:
            return self.encode_aes(msg)

    def encode_aes(self, msg):
        # msg = self.byte_pad(msg)
        # msg_len = len(msg)
        # need_len = msg_len % 16
        # if need_len != 0:
        #     need_len = 16 - need_len
        #     msg += " " * need_len
        return self.aes_obj.encrypt(pad(msg))

    def decode_aes(self, msg):
        try:
            print "decode_aes:", [msg]
            # decode_msg = self.byte_unpad(self.aes_obj.decrypt(msg))
            decode_msg = unpad(self.aes_obj.decrypt(msg))
        except Exception, e:
            print "decode_aes error", [msg]
            return None

        msg_len = len(decode_msg)
        print "msg_len:", msg_len, [decode_msg]
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
        print "bytePad:", add_num
        return text + chr(add_num) * add_num

    def byte_unpad(self,text, byteAlignLen=16):
        count = len(text)
        print "byteUnpad:", count
        mod_num = count % byteAlignLen
        assert mod_num == 0
        lastChar = text[-1]
        lastLen = ord(lastChar)
        lastChunk = text[-lastLen:]
        if lastChunk == chr(lastLen) * lastLen:
            # print "byteUnpad"
            return text[:-lastLen]
        return text


if __name__ == "__main__":
    ret = AesEncoder().encode(json.dumps({"user_id": 1, "passwd":"123456"}))
    ret2 = AesEncoder().decode(ret)
    print ret
    print [ret2]