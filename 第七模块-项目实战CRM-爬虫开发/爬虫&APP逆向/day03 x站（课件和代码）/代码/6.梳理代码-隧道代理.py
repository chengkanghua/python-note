import requests
import uuid
import time
import random

import requests


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


def get_tunnel_proxies():
    proxy_host = 'tps135.kdlapi.com:15818'
    proxy_username = 't12909832214236290'
    proxy_pwd = 'sdfsdfsdffsd'

    return {
        "http": "http://{}:{}@{}".format(proxy_username, proxy_pwd, proxy_host),
        "https": "https://{}:{}@{}".format(proxy_username, proxy_pwd, proxy_host),
    }


class PcAnonymous(object):
    """ 匿名pc播放"""

    def __init__(self, aid, bvid, cid, view_count, duration, proxies):
        self.aid = aid
        self.bvid = bvid
        self.cid = cid
        self.view_count = view_count
        self.duration = duration

        self.session = requests.Session()
        self.session.proxies = proxies
        self.session.headers = {
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",
        }

        self._uuid = self.gen_uuid()
        self.start_ts = None

    def gen_uuid(self):
        uuid_sec = str(uuid.uuid4())
        time_sec = str(int(time.time() * 1000 % 1e5))
        time_sec = time_sec.ljust(5, "0")

        return "{}{}infoc".format(uuid_sec, time_sec)

    def gen_buvid3(self):
        url = "https://www.bilibili.com/video/{}".format(self.bvid)
        res = self.session.get(
            url=url
        )
        res.close()

    def gen_bfe_id(self):
        self.session.cookies['_uuid'] = self._uuid
        self.session.cookies['CURRENT_FNVAL'] = "80"
        self.session.cookies['blackside_state'] = "1"
        res = self.session.get(
            url='https://api.bilibili.com/x/web-interface/nav'
        )
        res.close()

    def gen_sid(self):
        res = self.session.get(
            url="https://api.bilibili.com/x/player/v2",
            params={
                'cid': self.cid,  # 可以通过一些其他的接口直接获取到
                'aid': self.aid,
                'bvid': self.bvid,
            }
        )
        res.close()

    def click_now(self):
        res = self.session.get(
            url="https://api.bilibili.com/x/click-interface/click/now",
            params={
                "jsonp": "jsonp"
            }
        )
        self.start_ts = res.json()['data']['now']

    def click_web_h5(self):
        self.start_ts = start_ts = int(time.time())
        res = self.session.post(
            url="https://api.bilibili.com/x/click-interface/click/web/h5",
            data={
                "aid": self.aid,
                "cid": self.cid,
                "bvid": self.bvid,
                "part": "1",
                "mid": "0",
                "lv": "0",
                "ftime": start_ts - random.randint(10, 200),  # 浏览器首次打开时间
                "stime": start_ts,
                "jsonp": "jsonp",
                "type": "3",
                "sub_type": "0",
                "from_spmid": "",
                "auto_continued_play": "0",
                "refer_url": "",
                "bsource": "",
                "spmid": ""
            }
        )

        res.close()

    def first_heartbeat(self):
        res = self.session.post(
            url="https://api.bilibili.com/x/click-interface/web/heartbeat",
            data={
                "aid": self.aid,
                "cid": self.cid,
                "bvid": self.bvid,
                "mid": "0",
                "csrf": "",
                "played_time": "0",
                "real_played_time": "0",
                "realtime": "0",
                "start_ts": self.start_ts,
                "type": "3",
                "dt": "2",
                "play_type": "1",
                "from_spmid": "",
                "spmid": "",
                "auto_continued_play": "0",
                "refer_url": "",
                "bsource": ""
            }
        )

        res.close()

    def run(self):
        try:
            self.gen_buvid3()
            self.gen_bfe_id()
            self.gen_sid()
            # self.click_now()
            self.click_web_h5()
            self.first_heartbeat()
        except Exception as e:
            print("请求异常：", e)


def handler():
    proxies = get_tunnel_proxies()

    # 1.用户输入视频buvid
    buvid = "BV1Mb4y1X73e"

    # 2.获取视频信息
    aid, bvid, cid, view_count, duration = get_video_info(buvid)

    # 3.播放
    pc = PcAnonymous(aid, bvid, cid, view_count, duration, proxies)
    pc.run()


if __name__ == '__main__':
    handler()
