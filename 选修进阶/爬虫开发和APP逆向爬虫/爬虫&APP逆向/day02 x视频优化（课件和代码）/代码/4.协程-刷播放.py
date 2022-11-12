import time
import random
import datetime
import aiohttp
import asyncio
from urllib.parse import parse_qs, urlparse, urlencode
import execjs
import ctypes
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
import binascii

HEADERS = {
    'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                  'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
    'referer': 'https://m.yangshipin.cn/',
}

javascript_file = execjs.compile('''
function createGUID() {
    var e = (new Date).getTime().toString(36)
      , t = Math.random().toString(36).replace(/^0./, "");
    return "".concat(e, "_").concat(t)
}
''')


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
    return binascii.b2a_hex(aes_bytes).decode().upper()


def create_qa(data_string):
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
    for i in data_string:
        _char = ord(i)
        a = (a << 5) - a + _char
        # a &= a & 0xffffffff
        a &= a
    return ctypes.c_int32(a).value


def create_ckey(vid, rnd, app_ver, platform, guid):
    wt = "mg3c3b04ba"
    ending = "https://w.yangshipin.cn/|mozilla/5.0 (macintosh; ||Mozilla|Netscape|MacIntel|"

    data_list = ["", vid, rnd, wt, app_ver, guid, platform, ending]
    string = "|".join(data_list)
    qa = create_qa(string)
    encrypt_string = "|{}{}".format(qa, string)
    ckey = "--01" + aes_encrypt(encrypt_string).upper()
    return ckey


async def fetch_vkey(session, vid, rnd, app_ver, platform, flow_id, guid, ckey):
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

    async with session.get(url=url, params=params, headers=headers) as res:
        text = await res.text() # IO等待
        fn, vkey = eval(text)
        return fn, vkey


def txplayerJsonpCallBack_getinfo_711482(arg):
    return arg['vl']['vi'][0]['fn'], arg['vl']['vi'][0]['fvkey']


async def play(session, video_url, vid, pid, guid, fn, vkey):
    download_params = {
        "sdtfrom": "v7007",
        "guid": guid,
        "vkey": vkey,
        "platform": "2",
    }
    # 视频下载连接视频
    download_url = "https://mp4playcloud-cdn.ysp.cctv.cn/{}?{}".format(fn, urlencode(download_params))

    # 播放视频
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
        "vurl": download_url,
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
    url = "https://btrace.yangshipin.cn/kvcollect"
    async with session.post(url=url, params=params, data=data, headers=HEADERS) as res:
        text = await res.text() # IO等待
        print(text)


async def handler(video_url):
    try:
        async with aiohttp.ClientSession() as session:
            platform = "4330701"
            app_ver = "1.3.5"
            rnd = str(int(time.time()))
            vid = parse_qs(urlparse(video_url).query)['vid'][0]
            guid = javascript_file.call('createGUID')
            pid = javascript_file.call('createGUID')
            flow_id = "{}_{}".format(pid, platform)
            ckey = create_ckey(vid, rnd, app_ver, platform, guid)

            # 网络请求
            fn, vkey = await fetch_vkey(session, vid, rnd, app_ver, platform, flow_id, guid, ckey)

            await play(session, video_url, vid, pid, guid, fn, vkey)

    except Exception as e:
        print(e)


async def engine(video_url):
    # 创建100个任务
    tasks = [
        asyncio.create_task(handler(video_url)) for _ in range(100)
    ]
    await asyncio.wait(tasks)


def task(video_url):
    # import platform
    # if "Windows" in platform.platform():
    #     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    # engine(video_url)协程对象
    asyncio.run(engine(video_url))


if __name__ == '__main__':
    task("https://w.yangshipin.cn/video?type=0&vid=u000058lp0z&ptag=yangshipincp")
