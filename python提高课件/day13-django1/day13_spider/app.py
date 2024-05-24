"""
ckey是基于aes算法搞出来一个字符串。
    |qa|vid|时间戳|wt|version|guid|platform|https://w.yangshipin.cn/|mozilla/5.0 (macintosh; ||Mozilla|Netscape|MacIntel|
"""
import re
import time
import json
import datetime
import random
import binascii
import ctypes
from threading import RLock
from urllib.parse import urlencode, urlparse, parse_qs
from concurrent.futures import ThreadPoolExecutor
import redis
# 内部依赖 node.js
import execjs
import requests
from Crypto.Cipher import AES

javascript_file = execjs.compile('''
function A(t) {
    var e = (t ? new Date(t) : new Date).getTime().toString(36)
      , n = Math.random().toString(36).replace(/^0./, "");
    return "".concat(e, "_").concat(n)
}

function createGUID(e) {
    e = e || 32;
    for (var t = "", r = 1; r <= e; r++) {
        t += Math.floor(16 * Math.random()).toString(16);
    }
    return t;
}

function getTimeStampStr(e) {
    e = e || 10;
    var t = "".concat(parseInt(+new Date));
    if (t.length === e)
        return t;
    if (t.length > e)
        return t.substring(0, e);
    for (var r = e - t.length; r > 0; )
        t = "0".concat(t),
        r--;
    return t
}

function getJsonpCallbackName(e) {
    return ["txplayerJsonpCallBack", e, parseInt(1e6 * Math.random())].join("_")
}
''')


def create_qa(string):
    """
    string = "|d000035rirv|1622526980|mg3c3b04ba|1.3.2|df553a055bb06eda3653173ee5a010bf|4330701|https://w.yangshipin.cn/|mozilla/5.0 (macintosh; ||Mozilla|Netscape|MacIntel|"
    原算法
        Aa = "|d000035rirv|1622526980|mg3c3b04ba|1.3.2|df553a055bb06eda3653173ee5a010bf|4330701|https://w.yangshipin.cn/|mozilla/5.0 (macintosh; ||Mozilla|Netscape|MacIntel|"
        wl = -5516
        $a=0
        for (Se = 0; Se < Aa[St]; Se++)
                Ma = Aa[bt](Se), Ae["charCodeAt"]()
                $a = ($a << wl + 1360 + 9081 - 4920) - $a + Ma,
                $a &= $a;
            qa = $a
    """

    a = 0
    for i in string:
        _char = ord(i)
        a = (a << 5) - a + _char
        a &= a & 0xffffffff
    return ctypes.c_int32(a).value


def aes_encrypt(text):
    """
    AES加密
    """
    # "4E2918885FD98109869D14E0231A0BF4"
    # "16B17E519DDD0CE5B79D7A63A4DD801C"

    key = binascii.a2b_hex('4E2918885FD98109869D14E0231A0BF4')
    iv = binascii.a2b_hex('16B17E519DDD0CE5B79D7A63A4DD801C')
    pad = 16 - len(text) % 16
    text = text + pad * chr(pad)
    text = text.encode()
    cipher = AES.new(key, AES.MODE_CBC, iv)
    encrypt_bytes = cipher.encrypt(text)
    return binascii.b2a_hex(encrypt_bytes).decode()


def create_wt():
    """
    h5_plugins.js文件
    for (Wt = "",
        Kt = xc + yc + -7598 + 4607,
        zt = cs + "৮঺৪঺৫হঽ৫২"; Kt < zt.length; Kt++)
            Wt += String["f" + ls + "de"](-1746 + Hc + 14157 ^ zt[ps + us + "CodeAt"](Kt));
    """
    return "mg3c3b04ba"


def create_version():
    """
        播放器版本 TenVideoPlayer_V3.js
    """
    return "1.3.2"


def create_ckey(vid, tt, version, platform, guid):
    wt = create_wt()
    ending = "https://w.yangshipin.cn/|mozilla/5.0 (macintosh; ||Mozilla|Netscape|MacIntel|"

    data_list = ["", vid, tt, wt, version, guid, platform, ending]
    string = "|".join(data_list)
    qa = create_qa(string)
    encrypt_string = "|{}{}".format(qa, string)
    ckey = "--01" + aes_encrypt(encrypt_string).upper()
    return ckey


def fetch_vkey(vid, rnd, app_ver, platform, flow_id, guid, ckey):
    params = {
        "callback": "txplayerJsonpCallBack_getinfo_711482",
        "charge": "0",
        "defaultfmt": "auto",
        "otype": "json",
        "guid": guid,
        "flowid": flow_id,
        "platform": platform,
        "sdtfrom": "v7007",
        "defnpayver": "0",
        "appVer": app_ver,
        "host": "w.yangshipin.cn",
        "ehost": "https://w.yangshipin.cn/video",
        "refer": "w.yangshipin.cn",
        "sphttps": "1",
        "_rnd": rnd,  # _rnd: x.getTimeStampStr(),
        "spwm": "4",
        "vid": vid,
        "defn": "auto",
        "show1080p": "false",
        "dtype": "1",
        "clip": "4",
        "fmt": "auto",
        "defnsrc": "",
        "fhdswitch": "",
        "defsrc": "1",
        "sphls": "",
        "encryptVer": "8.1",
        "cKey": ckey,
    }

    headers = {
        'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                      'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
        'referer': 'https://m.yangshipin.cn/',
    }

    res = requests.get(
        url="https://playvv.yangshipin.cn/playvinfo",
        params=params,
        headers=headers
    )
    res.close()
    text = res.text.strip("txplayerJsonpCallBack_getinfo_711482")[1:-1]
    res_dict = json.loads(text)
    return res_dict


def run(video_url):
    platform = "4330701"
    app_ver = "1.3.2"
    rnd = str(int(time.time()))

    vid = parse_qs(urlparse(video_url).query)['vid'][0]
    guid = javascript_file.call('createGUID')
    pid = javascript_file.call('createGUID')
    flow_id = "{}_{}".format(pid, platform)

    ckey = create_ckey(vid, rnd, app_ver, platform, guid)
    vkey_info = fetch_vkey(vid, rnd, app_ver, platform, flow_id, guid, ckey)

    txplayerJsonpCallBack_getinfo_711482(vkey_info, video_url, vid, guid, pid)


def txplayerJsonpCallBack_getinfo_711482(response, video_url, vid, guid, pid):
    params = {
        "sdtfrom": "v7007",
        "guid": guid,
        "vkey": response["vl"]['vi'][0]['fvkey'],
        "platform": "2",
    }

    # 视频下载连接视频
    download_video_url = "https://mp4playcloud-cdn.ysp.cctv.cn/{}.iHMg10002.mp4?{}".format(vid, urlencode(params))

    # 播放视频
    res = requests.post(
        url="https://btrace.yangshipin.cn/kvcollect",
        params={
            "BossId": 2865,
            "Pwd": 1698957057,
            "_dc": random.random()  # "&_dc=".concat(Math.random()))
        },
        data={
            "uin": "",
            "vid": vid,
            "coverid": "",
            "pid": pid,
            "guid": guid,
            "unid": "",
            "vt": "0",
            "type": "3",
            # "url": "https://w.yangshipin.cn/video?type=0&vid=d000035rirv",
            "url": video_url,
            "bi": "0",
            "bt": "0",
            "version": "1.3.2",
            "platform": "4330701",
            "defn": "0",
            # "ctime": "2021-06-02 09:30:01",
            "ctime": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "ptag": "",
            "isvip": "-1",
            "tpid": "13",
            "pversion": "h5",
            "hc_uin": "",
            "hc_vuserid": "",
            "hc_openid": "",
            "hc_appid": "",
            "hc_pvid": "0",
            "hc_ssid": "",
            "hc_qq": "",
            "hh_ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML  like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "ua": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML  like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "ckey": "",
            "iformat": "0",
            "hh_ref": video_url,
            "vuid": "",
            "vsession": "",
            "format_ua": "other",
            "common_rcd_info": "",
            "common_ext_info": "",
            "v_idx": "0",
            "rcd_info": "",
            "extrainfo": "",
            "c_channel": "",
            "vurl": download_video_url,
            "step": "6",
            "val": "164",
            "val1": "1",
            "val2": "1",
            "idx": "0",
            "c_info": "",
            "isfocustab": "0",
            "isvisible": "0",
            "fact1": "",
            "fact2": "",
            "fact3": "",
            "fact4": "",
            "fact5": "",
            "cpay": "0",
            "tpay": "0",
            "dltype": "1"
        },
        headers={
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                          'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'referer': 'https://m.yangshipin.cn/',
        }
    )
    res.close()


def get_old_view_count(url):
    res = requests.get(
        url=url,
        headers={
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                          'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'referer': 'https://m.yangshipin.cn/',
        }
    )

    data = re.findall(r'"subtitle":"(.+)次观看","', res.text)[0]
    return data


def execute():
    # 1.基于redis去队列中获取订单
    conn = redis.Redis(host='127.0.0.1', port=6379, password="qwe123")
    conn.lpush("video_order_list", "20210620160226102096")

    while True:
        # 消费者，去队列中获取数据，如果没有任务默认是返回 None
        _, oid = conn.brpop("video_order_list")
        oid = oid.decode('utf-8')  # 获取到订单ID

        # 2.根据订单ID去数据库中获取订单的 URL、要刷的数据（pymysql去做）
        """
            2.1 连接数据库读取数据
            2.2 获取count，url = select * from app01_order where oid=%s    oid
        """
        count = 1000
        url = "https://w.yangshipin.cn/video?type=0&vid=s000034o5z2"

        # 3. 爬虫根据url获取原播放量【重点】
        old_count = get_old_view_count(url)

        # 4. 连接数据库：status=2，原播放量=爬虫获取的数据=万次观看

        # 5. 开始去爬取数据【重点】
        # 1s刷1个，  60*60*24 = 86400 = 25元
        # 1s刷100个, 60*60*24 = 86400 = 2500元
        pool = ThreadPoolExecutor(100)
        for i in range(count):
            pool.submit(run, url)
        pool.shutdown()

        # 6. 连接数据库：status=3


if __name__ == '__main__':
    execute()
