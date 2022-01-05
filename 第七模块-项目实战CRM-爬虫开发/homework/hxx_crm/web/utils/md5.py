import hashlib

def gen_md5(origin):
    """
    md5加密
    """
    ha = hashlib.md5(b'sdfsg3')
    ha.update(origin.encode('utf-8'))
    return ha.hexdigest()

