import base64
import requests
import re
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import string
import random
import time
import hashlib

SALT = "9cafa6466a028bfb"
KEY = "fd6b639dbcff0c2a1b03b389ec763c4b"
IV = "77b07a672d57d64c"


def get_video_info(bvid):
    session = requests.Session()
    res = session.get(
        url="https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp".format(bvid),
    )
    cid = res.json()['data'][0]['cid']

    res = session.get(
        url="https://api.bilibili.com/x/web-interface/view?cid={}&bvid={}".format(cid, bvid),
    )
    res_json = res.json()
    aid = res_json['data']['aid']
    view_count = res_json['data']['stat']['view']
    # total_duration = res_json['data']['duration'] # 总时长
    duration = res_json['data']['pages'][0]['duration']  # 当前视频长度

    return aid, bvid, cid, view_count, duration


def create_random_mac(sep=":"):
    """ 随机生成mac地址 """

    def mac_same_char(mac_string):
        v0 = mac_string[0]
        index = 1
        while index < len(mac_string):
            if v0 != mac_string[index]:
                return False
            index += 1
        return True

    data_list = []
    for i in range(1, 7):
        part = "".join(random.sample("0123456789ABCDEF", 2))
        data_list.append(part)
    mac = sep.join(data_list)

    if not mac_same_char(mac) and mac != "00:90:4C:11:22:33":
        return mac

    return create_random_mac(sep)


def create_device_id(mac):
    """
    根据mac地址生成 3.device_id
    :param mac: 传入参数的格式是 00:00:00:00:00
    :return:
    """

    def gen_sn():
        return "".join(random.sample("123456789" + string.ascii_lowercase, 10))

    def base64_encrypt(data_string):
        data_bytes = bytearray(data_string.encode('utf-8'))
        data_bytes[0] = data_bytes[0] ^ (len(data_bytes) & 0xFF)
        for i in range(1, len(data_bytes)):
            data_bytes[i] = (data_bytes[i - 1] ^ data_bytes[i]) & 0xFF
        res = base64.encodebytes(bytes(data_bytes))
        return res.strip().strip(b"==").decode('utf-8')

    # 1. 生成mac地址（保证mac中的每个元素是不重复的，例如：0000000000)
    mac_str = mac

    # 2. 去除IP地址中的符号，只保留 48e1e828e02e（变小写）
    mac_str = re.sub("[^0-9A-Fa-f]", "", mac_str)
    mac_str = mac_str.lower()

    # 3. 获取手续序列号
    sn = gen_sn()

    # 4. 拼接并进行base64加密
    total_string = "{}|||{}".format(mac_str, sn)
    return base64_encrypt(total_string)


def sha_256_encrypt(data_string):
    sha = hashlib.sha256()
    sha.update(data_string.encode('utf-8'))
    sha.update(SALT.encode('utf-8'))
    return sha.hexdigest()


def aes_encrypt(data_string):
    aes = AES.new(
        key=KEY.encode('utf-8'),
        mode=AES.MODE_CBC,
        iv=IV.encode('utf-8')
    )
    raw = pad(data_string.encode('utf-8'), 16)
    return aes.encrypt(raw)


def run():
    mac_string = create_random_mac().upper()
    device_id = create_device_id(mac_string)

    aid, bvid, cid, view_count, duration = get_video_info("BV1Mb4y1X73e")

    ctime = int(time.time())
    info = {
        'aid': aid,
        'cid': cid,
        'part': 1,
        'mid': 0,
        'lv': 0,
        'ftime': ctime - random.randint(100, 1000),
        'stime': ctime,
        'did': device_id,
        'type': 3,
        'sub_type': 0,
        'sid': '0',
        'epid': '',
        'auto_play': 0,
        'build': 6240300,
        'mobi_app': 'android',
        'spmid': 'main.ugc-video-detail.0.0',
        'from_spmid': 'search.search-result.0.0'
    }
    data = "&".join(["{}={}".format(key, info[key]) for key in sorted(info.keys())])
    sign = sha_256_encrypt(data).lower()
    data = "{}&sign={}".format(data, sign)
    aes_string = aes_encrypt(data)
    print(aes_string)


if __name__ == '__main__':
    run()
