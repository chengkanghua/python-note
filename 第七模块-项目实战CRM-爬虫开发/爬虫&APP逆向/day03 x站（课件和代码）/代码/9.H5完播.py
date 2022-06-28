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


class H5Anonymous(object):
    """ 匿名h5播放"""

    def __init__(self, aid, bvid, cid, view_count, duration, proxies):
        self.aid = aid
        self.bvid = bvid
        self.cid = cid
        self.view_count = view_count
        self.duration = duration

        self.session = requests.Session()
        self.session.proxies = proxies
        self.session.headers = {
            "user-agent": "Mozilla/5.0 (Linux; Android 5.0; SM-G900P Build/LRX21T) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Mobile Safari/537.36",
        }

        self._uuid = self.gen_uuid()
        self.start_ts = None

    def gen_uuid(self):
        uuid_sec = str(uuid.uuid4())
        time_sec = str(int(time.time() * 1000 % 1e5))
        time_sec = time_sec.ljust(5, "0")

        return "{}{}infoc".format(uuid_sec, time_sec)

    def gen_buvid3(self):
        url = "https://m.bilibili.com/video/{}".format(self.bvid)
        res = self.session.get(
            url=url
        )
        res.close()

    def gen_bfe_id(self):
        res = self.session.get(
            url='https://api.bilibili.com/x/web-interface/nav'
        )
        res.close()

    def gen_sid(self):
        self.session.cookies['_uuid'] = self._uuid
        res = self.session.get(
            url="https://api.bilibili.com/x/player/v2",
            params={
                'cid': self.cid,  # 可以通过一些其他的接口直接获取到
                'aid': self.aid,
                'ep_id': 0,
                'season_id': 0,
            }
        )
        res.close()

    def click_now(self):
        res = self.session.get(
            url="https://api.bilibili.com/x/report/click/now",
            params={
                "jsonp": "jsonp"
            }
        )
        self.start_ts = res.json()['data']['now']

    def click_h5(self):
        self.start_ts = start_ts = int(time.time())
        res = self.session.post(
            url="https://api.bilibili.com/x/click-interface/click/h5",
            data={
                "aid": self.aid,
                "cid": self.cid,
                "bvid": self.bvid,
                "part": "1",
                "did": self.session.cookies['sid'],
                "mid": "",
                "lv": "0",
                "ftime": start_ts - random.randint(10, 200),  # 浏览器首次打开时间
                "stime": start_ts,
                "jsonp": "jsonp",
                "type": "3",
                "sub_type": "0",
                "from_spmid": "undefined",
                "spmid": "333.401.0.0"
            }
        )

        res.close()

    def first_heartbeat(self):
        res = self.session.post(
            url="https://api.bilibili.com/x/report/web/heartbeat",
            data={
                "aid": self.aid,
                "cid": self.cid,
                "bvid": self.bvid,
                "csrf": "",
                "played_time": "0",
                "realtime": "0",
                "start_ts": self.start_ts,
                "type": "3",
                "dt": "7",
                "play_type": "1",
                "spmid": "333.401.0.0",
                "refer": "https://m.bilibili.com/video/{}".format(self.bvid),
            }
        )

        res.close()

    def heartbeat(self):

        loop_count, div = divmod(self.duration, 15)
        if div == 0:
            div = 15
            loop_count -= 1

        for i in range(1, loop_count + 1):
            interval_time = i * 15
            time.sleep(15)
            data_dict = {
                "aid": self.aid,
                "cid": self.cid,
                "bvid": self.bvid,
                "csrf": "",
                "played_time": interval_time,
                "realtime": interval_time,
                "start_ts": self.start_ts,
                "type": "3",
                "dt": "7",
                "play_type": "0",
                "spmid": "333.401.0.0",
                "refer": "https://m.bilibili.com/video/{}".format(self.bvid),
            }

            res = self.session.post(
                url="https://api.bilibili.com/x/report/web/heartbeat",
                data=data_dict
            )
            res.close()

        time.sleep(div)

        data_dict = {
            "aid": self.aid,
            "cid": self.cid,
            "bvid": self.bvid,
            "csrf": "",
            "played_time": -1,
            "realtime": self.duration,
            "start_ts": self.start_ts,
            "type": "3",
            "dt": "7",
            "play_type": "0",
            "spmid": "333.401.0.0",
            "refer": "https://m.bilibili.com/video/{}".format(self.bvid),
        }

        res = self.session.post(
            url="https://api.bilibili.com/x/report/web/heartbeat",
            data=data_dict
        )
        res.close()
        
    def run(self):
        try:
            self.gen_buvid3()
            self.gen_bfe_id()
            self.gen_sid()
            # self.click_now()
            self.click_h5()
            self.first_heartbeat()

            # 心跳
            self.heartbeat()
        except Exception as e:
            print("请求异常：", e)


def handler():
    # 1.用户输入视频buvid
    buvid = "BV1Mb4y1X73e"

    # 2.获取视频信息
    aid, bvid, cid, view_count, duration = get_video_info(buvid)

    # 3.播放
    h5 = H5Anonymous(aid, bvid, cid, view_count, duration, None)
    h5.run()


if __name__ == '__main__':
    handler()
