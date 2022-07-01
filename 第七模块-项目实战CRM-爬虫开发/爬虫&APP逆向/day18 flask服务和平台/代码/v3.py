"""
    1. 签名时，自动会生成ts字段
    2. ts比当前时间小 1000s

"""
import datetime
import time
import base64
import hashlib
import time
import requests
import random
import re
import json
import rsa
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from urllib.parse import quote_plus
import string
import random
import time
import hashlib
import ctypes


class BiliBili(object):
    def __init__(self, aid, bvid, cid, duration, server_host):
        self.aid, self.bvid, self.cid, self.duration = aid, bvid, cid, duration

        self.wifi_mac = self.create_random_mac().upper()
        self.device_id = self.create_device_id(self.wifi_mac)
        self.buvid = self.create_buvid_by_wifi()
        self.android_id = self.create_random_mac(sep="").lower()
        self.session_id = self.create_session_id()

        self.build_brand = "HUAWEI"
        self.build_model = 'Mate 10 Pro'

        self.fp_local = self.create_local(self.buvid, self.build_model, "")
        self.fp_remote = self.create_local(self.buvid, self.build_model, "")

        self.build_fingerprint = "OnePlus/OnePlus2/OnePlus2:6.0.1/MMB29M/1447841200:user/release-keys"
        self.build_display = "V417IR release-keys"
        self.app_first_run_time = str(int(time.time()) - random.randint(0, 24 * 60 * 60))  # fts

        self.cookie_dict = {}
        self.hash = None
        self.rsa_pub_key = None
        self.guest_id = None

        self.sign_task_url = "http://{}/sign/task/".format(server_host)
        self.sign_sign_url = "http://{}/sign/".format(server_host)

    @staticmethod
    def get_video_id_info(exec_url):

        session = requests.Session()
        bvid = exec_url.rsplit('/')[-1]
        res = session.get(
            url="https://api.bilibili.com/x/player/pagelist?bvid={}&jsonp=jsonp".format(bvid)
        )

        cid = res.json()['data'][0]['cid']

        res = session.get(
            url="https://api.bilibili.com/x/web-interface/view?cid={}&bvid={}".format(cid, bvid)
        )
        res_json = res.json()
        aid = res_json['data']['aid']
        view_count = res_json['data']['stat']['view']
        duration = res_json['data']['duration']
        session.close()
        return aid, bvid, cid, duration

    def create_random_mac(self, sep=":"):
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

        return self.create_random_mac(sep)

    def create_device_id(self, mac):
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

    def create_buvid_by_wifi(self):
        """
            基于wifi mac地址生成buvid （ B站app中有四种获取buvid的方式：设备ID、wifi mac地址、3.device_id、uuid ）
        """
        md5 = hashlib.md5()
        md5.update(self.wifi_mac.encode('utf-8'))
        v0_1 = md5.hexdigest()
        return "XY{}{}{}{}".format(v0_1[2], v0_1[12], v0_1[22], v0_1).upper()

    def create_session_id(self):
        return "".join([hex(item)[2:] for item in random.randbytes(4)])

    def create_heart_beat_session_id(self):
        def int_overflow(val):
            maxint = 2147483647
            if not -maxint - 1 <= val <= maxint:
                val = (val + (maxint + 1)) % (2 * (maxint + 1)) - maxint - 1
            return val

        def unsigned_right_shitf(n, i):
            # 数字小于0，则转为32位无符号uint
            if n < 0:
                n = ctypes.c_uint32(n).value
            # 正常位移位数是为正数，但是为了兼容js之类的，负数就右移变成左移好了
            if i < 0:
                return -int_overflow(n << abs(i))
            # print(n)
            return int_overflow(n >> i)

        arg0 = str(int(time.time() * 1000)) + str(random.randint(1, 1000000));
        # sha1加密
        hash_object = hashlib.sha1()
        hash_object.update(arg0.encode('utf-8'))
        arg7 = hash_object.digest()
        v8 = [-1 for i in range(len(arg7) * 2)]
        v0 = len(arg7)
        v1 = 0
        v2 = 0
        while v1 < v0:
            v3 = arg7[v1]
            v4 = v2 + 1
            v5 = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
            index = unsigned_right_shitf(v3, 4) & 15
            v8[v2] = v5[index]
            v2 = v4 + 1
            v8[v4] = v5[v3 & 15]
            # ++v1
            v1 += 1

        data = "".join(v8)
        return data.lower()

    def create_local(self, buvid, phone_model, phone_band):
        """
        fp_local和fp_remote都是用这个算法来生成的，在手机初始化阶段生成 fp_local，
        :param buvid: 根据算法生成的buvid，例如："XYBA4F3B2789A879EA8AEEDBE2E4118F78303"
        :param phone_model:  手机型号modal，例如："Mate 10 Pro"
        :param phone_band:  手机品牌band，在模拟器上是空字符串（我猜是程序员想要写成 brand ）哈哈哈哈
        :return:
        """

        def misc_helper_kt(data_bytes):
            data_list = []
            v7 = len(data_bytes)
            v0 = 0
            while v0 < v7:
                v2 = data_bytes[v0]
                data_list.append("%02x" % v2)
                v0 += 1
            return ''.join(data_list)

        data_string = "{}{}{}".format(buvid, phone_model, phone_band)
        hash_object = hashlib.md5()
        hash_object.update(data_string.encode('utf-8'))
        data = hash_object.digest()

        arg1 = misc_helper_kt(data)
        arg2 = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        arg3 = misc_helper_kt(random.randbytes(8))

        return "{}{}{}".format(arg1, arg2, arg3)

    def get_param_sign(self, param_dict, sign_type=1):
        """
            调用本地 flask服务+app 执行so文件，获取sign算法
        :param param_dict: 要签名的参数字典
        :param sign_type: 签名类型
                          sign_type=1，内部调用 LibBili.g 加密，参数：g(Map arg1)
                          sign_type=2，内部调用 LibBili.h 加密，参数：h(Map arg1, int arg2, int arg3)，暂时固定：arg2=1、arg3=0
        :return:
        """
        ordered_string = "&".join(["{}={}".format(key, param_dict[key]) for key in sorted(param_dict.keys())])
        # 调用so文件，根据 ordered_string 生成sign（基于flask server实现）
        # 任务发送给Flask
        res = requests.post(
            url=self.sign_task_url,
            data={
                'param_string': ordered_string,
                'sign_type': sign_type
            }
        )
        uid = res.text.strip()

        # 等待，签名结果
        res = requests.get(
            url=self.sign_sign_url,
            params={'uid': uid}
        )
        total_param_string = res.text.strip()
        return total_param_string

    def init_request(self):
        """
        初识请求
            1. 生成buvid（后续还继续用）并发送请求
            2. 获取cookie中的bfe_id
        """
        params = {
            'abi': 'x86',
            'appid': 'tv.danmaku.bili',
            'appkey': '1d8b6e7d45233436',
            'build': '6240300',
            'channel': 'bili',
            'env': 'prod',
            'iv': '6240300',
            'mobi_app': 'android',
            'brand': self.build_brand,
            'model': self.build_model,
            'nt': '1',
            'ov': '23',
            'screen': '1872_1170@416.0_416.0',
            'sn': '5398898',  # 未知
            'vn': '6.24.0',
            # 'sign': '044580bfa2e4d01a2d34b15908b92f79',   sign和ts有so文件自动生成
            # 'ts': str(int(time.time()))
        }
        total_param_string = self.get_param_sign(params)
        first_url = "https://app.bilibili.com/x/v2/version/fawkes/bizapk?{}".format(total_param_string)
        res = requests.get(
            url=first_url,
            headers={
                "user-agent": "Mozilla/5.0 BiliDroid/6.24.0 (bbcallen@gmail.com) os/android model/Mate 10 Pro mobi_app/android build/6240300 channel/bili innerVer/6240300 osVer/6.0.1 network/2",
                'app-key': 'android',
                'env': 'prod',
                'buvid': self.buvid
            }
        )
        self.cookie_dict.update(res.cookies.get_dict())

    def passport_web_key(self):
        """
        获取哈希和公钥，不知道什么作用。
        """
        info = {
            'build': '6240300',
            'appkey': "bca7e84c2d947ac6",  # 登录专用
            'mobi_app': 'android',
            'platform': 'android',
            'c_local': 'zh_CN',
            's_local': 'zh_CN',
            'channel': "bili",
        }
        total_param_string = self.get_param_sign(info, 2)

        first_url = "https://passport.bilibili.com/x/passport-login/web/key?{}".format(total_param_string)
        res = requests.get(
            url=first_url,
            headers={
                "user-agent": "Mozilla/5.0 BiliDroid/6.24.0 (bbcallen@gmail.com) os/android model/Mate 10 Pro mobi_app/android build/6240300 channel/bili innerVer/6240300 osVer/6.0.1 network/2",
                'app-key': 'android',
                'env': 'prod',
                'buvid': self.buvid
            }
        )
        self.hash = res.json()['data']['hash']
        self.rsa_pub_key = res.json()['data']['key']
        print("2.获取公钥 -> ", res.text)

    def passport_guest_reg(self):
        """ 游客注册，用于获取游客 GuestId """

        def get_random_string(count=16):
            ca = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
            char_list = []
            for v2 in range(count):
                char = random.choice(ca)
                char_list.append(char)
            return "".join(char_list)

        def aes_encrypt_to_hex_string(data, key, iv):
            aes = AES.new(
                key=key.encode('utf-8'),
                mode=AES.MODE_CBC,
                iv=iv.encode('utf-8')
            )
            raw = pad(data.encode('utf-8'), 16)
            encrypt_bytes = aes.encrypt(raw)
            hex_string = ''.join(['%02X' % b for b in encrypt_bytes])
            return hex_string

        def rsa_encrypt(message):
            """校验RSA加密 使用公钥进行加密"""
            key_bytes = self.rsa_pub_key.encode('utf-8')
            pk = rsa.PublicKey.load_pkcs1_openssl_pem(key_bytes)
            val = rsa.encrypt(message.encode('utf-8'), pk)
            return base64.standard_b64encode(val).decode('utf-8')

        # 1. 根据这个字典信息生成 dt 和 device_info（顺序不能乱）
        info = {
            "AndroidID": self.android_id,
            "BuildBrand": self.build_brand,
            "BuildDisplay": self.build_display,
            "BuildFingerprint": self.build_fingerprint,
            "BuildHost": "a11-gz02-test.i.nease.net",
            "Buvid": self.buvid,
            "DeviceType": "Android",
            "MAC": self.wifi_mac,
            "fts": self.app_first_run_time
        }
        data_string = json.dumps(info, separators=(',', ':'))
        random_string = get_random_string(16)
        device_info = aes_encrypt_to_hex_string(data_string, random_string, random_string)
        dt = rsa_encrypt(random_string)

        # 2.构造参数，调用 so 文件进行签名
        body = {
            'build': '6240300',
            'appkey': "bca7e84c2d947ac6",  # 登录专用
            'mobi_app': 'android',
            'platform': 'android',
            'c_local': 'zh_CN',
            's_local': 'zh_CN',
            'channel': "bili",
            'device_info': device_info,
            'dt': quote_plus(dt)
        }
        total_body_string = self.get_param_sign(body, 2)
        res = requests.post(
            url="https://passport.bilibili.com/x/passport-user/guest/reg",
            headers={
                "user-agent": "Mozilla/5.0 BiliDroid/6.24.0 (bbcallen@gmail.com) os/android model/Mate 10 Pro mobi_app/android build/6240300 channel/bili innerVer/6240300 osVer/6.0.1 network/2",
                'app-key': 'android',
                'env': 'prod',
                'buvid': self.buvid,
                "content-type": "application/x-www-form-urlencoded; charset=utf-8"
            },
            data=total_body_string.encode('utf-8')
        )
        self.guest_id = res.json()['data']['guest_id']
        print("3. 获取客户端ID -> ", res.text)

    def x_report_click_android2(self):
        SALT = "9cafa6466a028bfb"
        KEY = "fd6b639dbcff0c2a1b03b389ec763c4b"
        IV = "77b07a672d57d64c"

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

        ctime = int(time.time())
        info = {
            'aid': self.aid,
            'cid': self.cid,
            'part': 1,
            'mid': 0,
            'lv': 0,
            'ftime': ctime - random.randint(100, 1000),
            'stime': ctime,
            'did': self.device_id,
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

        res = requests.post(
            url="https://api.bilibili.com/x/report/click/android2",
            headers={
                "accept-length": "gzip",
                "content-type": "application/json; charset=utf-8",
                "app-key": "android",
                "User-Agent": "Mozilla/5.0 BiliDroid/6.24.0 (bbcallen@gmail.com) os/android model/Mate 10 Pro mobi_app/android build/6240300 channel/bili innerVer/6240300 osVer/6.0.1 network/2",
                "env": "prod",
                "buvid": self.buvid,
                "device-id": self.device_id,
                "session_id": self.session_id,
                "fp_local": self.fp_local,
                "fp_remote": self.fp_remote,
            },
            data=aes_string

        )
        res.close()
        print("4.点击播放视频 -> ", res.text)

    def heart_beat_start(self):

        form_dict = {
            "actual_played_time": "0",
            "aid": self.aid,
            "appkey": "1d8b6e7d45233436",
            "auto_play": "0",
            "build": "6240300",
            "c_locale": "zh_CN",
            "channel": "bili",
            "cid": self.cid,
            "epid": "0",
            "epid_status": "",
            "from": "2",
            "from_spmid": "main.ugc-video-detail.0.0",
            "last_play_progress_time": "0",
            "list_play_time": "0",
            "max_play_progress_time": "0",
            "mid": "0",
            "miniplayer_play_time": "0",
            "mobi_app": "android",
            "network_type": "1",
            "paused_time": "0",
            "platform": "android",
            "play_status": "0",
            "play_type": "1",
            "played_time": "0",
            "quality": "32",
            "s_locale": "zh_CN",
            "session": self.create_heart_beat_session_id(),
            "sid": "0",
            "spmid": "main.ugc-video-detail.0.0",
            "start_ts": "0",
            "statistics": quote_plus(
                json.dumps({"appId": 1, "platform": 3, "version": "6.24.0", "abtest": ""}, separators=(',', ':'))),
            "sub_type": "0",
            "total_time": "0",
            "type": "3",
            "user_status": "0",
            "video_duration": self.duration,
            # "ts": "1623544527",
            # "sign": "b098ca2c4caa53de22720a9755fde742"
        }

        total_body_string = self.get_param_sign(form_dict)

        res = requests.post(
            url="https://api.bilibili.com/x/report/heartbeat/mobile",
            headers={
                "accept-length": "gzip",
                "content-type": "application/x-www-form-urlencoded; charset=utf-8",
                "app-key": "android",
                "User-Agent": "Mozilla/5.0 BiliDroid/6.24.0 (bbcallen@gmail.com) os/android model/Mate 10 Pro mobi_app/android build/6240300 channel/bili innerVer/6240300 osVer/6.0.1 network/2",
                "env": "prod",
                "buvid": self.buvid,
                "device-id": self.device_id,
                "session_id": self.session_id,
                "fp_local": self.fp_local,
                "fp_remote": self.fp_remote,
            },
            data=total_body_string.encode('utf-8')

        )
        res.close()

        print("5.开始心跳 -> ", res.text)

    def heart_beat_end(self):

        form_dict = {
            "actual_played_time": self.duration,
            "aid": self.aid,
            "appkey": "1d8b6e7d45233436",
            "auto_play": "0",
            "build": "6240300",
            "c_locale": "zh_CN",
            "channel": "bili",
            "cid": self.cid,
            "epid": "0",
            "epid_status": "",
            "from": "2",
            "from_spmid": "main.ugc-video-detail.0.0",
            "last_play_progress_time": "0",
            "list_play_time": "0",
            "max_play_progress_time": "0",
            "mid": "0",
            "miniplayer_play_time": "0",
            "mobi_app": "android",
            "network_type": "1",
            "paused_time": "0",
            "platform": "android",
            "play_status": "0",
            "play_type": "1",
            "played_time": self.duration,
            "quality": "32",
            "s_locale": "zh_CN",
            "session": self.create_heart_beat_session_id(),
            "sid": "0",
            "spmid": "main.ugc-video-detail.0.0",
            "start_ts": "0",
            "statistics": quote_plus(
                json.dumps({"appId": 1, "platform": 3, "version": "6.24.0", "abtest": ""}, separators=(',', ':'))),
            "sub_type": "0",
            "total_time": self.duration,
            "type": "3",
            "user_status": "0",
            "video_duration": self.duration,
            # "ts": "1623544527",
            # "sign": "b098ca2c4caa53de22720a9755fde742"
        }

        total_body_string = self.get_param_sign(form_dict)

        res = requests.post(
            url="https://api.bilibili.com/x/report/heartbeat/mobile",
            headers={
                "accept-length": "gzip",
                "content-type": "application/x-www-form-urlencoded; charset=utf-8",
                "app-key": "android",
                "User-Agent": "Mozilla/5.0 BiliDroid/6.24.0 (bbcallen@gmail.com) os/android model/Mate 10 Pro mobi_app/android build/6240300 channel/bili innerVer/6240300 osVer/6.0.1 network/2",
                "env": "prod",
                "buvid": self.buvid,
                "device-id": self.device_id,
                "session_id": self.session_id,
                "fp_local": self.fp_local,
                "fp_remote": self.fp_remote,
            },
            data=total_body_string.encode('utf-8')

        )
        res.close()

        print("6.结束心跳 -> ", res.text)

    def x_v2_history_report(self):
        current_time = int(time.time())
        form_dict = {
            "aid": self.aid,
            "appkey": "1d8b6e7d45233436",
            "build": "6240300",
            "c_locale": "zh_CN",
            "channel": "bili",
            "cid": self.cid,
            "device_ts": current_time,
            "epid": "0",
            "mobi_app": "android",
            "platform": "android",
            # "progress": "-1", # -1，表示已播放完；时间表示播放了多久。
            "progress": self.duration - 10,  # -1，表示已播放完；时间表示播放了多久。
            "realtime": "0",
            "s_locale": "zh_CN",
            "sid": "0",
            "start_ts": current_time - self.duration - random.randint(1, 5),
            "statistics": quote_plus(
                json.dumps({"appId": 1, "platform": 3, "version": "6.24.0", "abtest": ""}, separators=(',', ':'))),
            "sub_type": "0",
            "type": "3",
            # "ts": "1623625703",
            # "sign": "67eac20b32ad7ef75d72391a89ac1aed"
        }

        total_body_string = self.get_param_sign(form_dict)
        res = requests.post(
            url="https://api.bilibili.com/x/v2/history/report",
            headers={
                "accept-length": "gzip",
                "content-type": "application/x-www-form-urlencoded; charset=utf-8",
                "app-key": "android",
                "User-Agent": "Mozilla/5.0 BiliDroid/6.24.0 (bbcallen@gmail.com) os/android model/Mate 10 Pro mobi_app/android build/6240300 channel/bili innerVer/6240300 osVer/6.0.1 network/2",
                "env": "prod",
                "buvid": self.buvid,
                "device-id": self.device_id,
                "session_id": self.session_id,
                "fp_local": self.fp_local,
                "fp_remote": self.fp_remote,
            },
            data=total_body_string.encode('utf-8')

        )
        res.close()

        print("7.播放完成的记录（退出播放界面时触发） -> ", res.text)


if __name__ == '__main__':
    flask_server_host = "192.168.0.6:5000"

    url = "https://www.bilibili.com/video/BV19K4y1H77x"

    # 1.获取视频的基本信息
    aid, bvid, cid, duration = BiliBili.get_video_id_info(url)

    # 2.实例化BiliBili类的对象
    bili = BiliBili(aid, bvid, cid, duration, flask_server_host)

    # 3.初始化请求
    bili.init_request()  # 算法1

    # 4.获取webkey
    bili.passport_web_key()  # 算法2
    bili.passport_guest_reg()  # 算法2
    bili.x_report_click_android2()  # 算法1
    bili.heart_beat_start()  # 算法1
    bili.heart_beat_end()  # 算法1
    bili.x_v2_history_report()  # 算法1
