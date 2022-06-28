import time
import random
import ctypes
import datetime
import binascii
from urllib.parse import urlparse, parse_qs, urlencode
from concurrent.futures import ThreadPoolExecutor

import execjs
import requests
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

javascript_file = execjs.compile('''
function createGUID() {
    var e = (new Date).getTime().toString(36)
      , t = Math.random().toString(36).replace(/^0./, "");
    return "".concat(e, "_").concat(t)
}
''')


def create_qa(data_string):
    """
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
    for i in data_string:
        _char = ord(i)
        a = (a << 5) - a + _char
        a &= a
    return ctypes.c_int32(a).value


def aes_encrypt(data_string):
    key = binascii.a2b_hex("4E2918885FD98109869D14E0231A0BF4")
    iv = binascii.a2b_hex("16B17E519DDD0CE5B79D7A63A4DD801C")
    aes = AES.new(
        key=key,
        mode=AES.MODE_CBC,
        iv=iv
    )
    raw = pad(data_string.encode('utf-8'), 16)
    aes_bytes = aes.encrypt(raw)
    return binascii.b2a_hex(aes_bytes).decode()


def create_ckey(vid, rnd, app_version, guid, platform):
    wt = "mg3c3b04ba"
    ending = "https://w.yangshipin.cn/|mozilla/5.0 (macintosh; ||Mozilla|Netscape|MacIntel|"

    # 1.拼接字符串
    data_list = ["", vid, rnd, wt, app_version, guid, platform, ending]
    data_string = "|".join(data_list)
    # 根据data_string生成qa
    qa = create_qa(data_string)
    encrypt_string = "|{}{}".format(qa, data_string)

    # 2.AES加密
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

    url = "https://playvv.yangshipin.cn/playvinfo"

    with requests.get(url=url, params=params, headers=headers) as res:
        # txplayerJsonpCallBack_getinfo_711482(  {"dltype":1,"exem":0}  } )
        # 1.去掉函数名和括号，再进行json序列化
        # json.loads(res.text[1:-1])
        # 返回的是个原组吧
        # print(res.text)
        # data = json.loads(res.text)
        # print(data)\
        # 假设内部都是单引号，这一句也会报错。
        # json.loads(res.text[1:-1])
        # 2.evel直接编译并执行函数
        return eval(res.text)


def txplayerJsonpCallBack_getinfo_711482(info_dict):
    return info_dict['vl']['vi'][0]['fn'], info_dict['vl']['vi'][0]['fvkey']


def play(video_url, vid, pid, guid, fn, vkey):
    download_params = {
        "sdtfrom": "v7007",
        "guid": guid,
        "vkey": vkey,
        "platform": "2",
    }
    # 视频下载连接视频
    vurl = "https://mp4playcloud-cdn.ysp.cctv.cn/{}?{}".format(fn, urlencode(download_params))

    params = {
        "BossId": 2865,
        "Pwd": 1698957057,
        "_dc": random.random()  # "&_dc=".concat(Math.random()))
    }
    data = {
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
        "vurl": vurl,
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
    }

    res = requests.post(
        url="https://btrace.yangshipin.cn/kvcollect",
        params=params,
        data=data,
        headers={
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                          'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'referer': 'https://m.yangshipin.cn/',
        }
    )
    print(res.text)
    res.close()


def run(video_url):
    vid = parse_qs(urlparse(video_url).query)['vid'][0]
    app_version = "1.3.5"
    platform = "4330701"
    guid = javascript_file.call('createGUID')
    pid = javascript_file.call('createGUID')
    flow_id = "{}_{}".format(pid, platform)
    rnd = str(int(time.time()))

    # 1.创建ckey
    ckey = create_ckey(vid, rnd, app_version, guid, platform)
    # 2.拿着ckey去发送请求从而获得
    # fn是资源地址  "u000058lp0z.ZKuq10002.mp4"
    # vkey=...
    fn, vkey = fetch_vkey(vid, rnd, app_version, platform, flow_id, guid, ckey)

    # 3.去播放
    play(video_url, vid, pid, guid, fn, vkey)


if __name__ == '__main__':
    url = "https://w.yangshipin.cn/video?type=0&vid=u000058lp0z&ptag=yangshipincp"
    pool = ThreadPoolExecutor(5)
    for i in range(2):
        pool.submit(run, url)

    pool.shutdown()
    print("完成")
