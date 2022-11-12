import requests
import time
import uuid
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


def gen_uuid():
    uuid_sec = str(uuid.uuid4())
    time_sec = str(int(time.time() * 1000 % 1e5))
    time_sec = time_sec.ljust(5, "0")

    return "{}{}infoc".format(uuid_sec, time_sec)


session = requests.Session()

session.headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36",

}

# 1.访问视频首页，获取 buvid3
url = "https://www.bilibili.com/video/BV1iq4y1p7LS"
res = session.get(
    url=url
)
res.close()
# print(session.cookies.get_dict())

# 2.访问nav，获取 bfe_id（需要cookie中携带 uuid + buvid3 + CURRENT_FNVAL + blackside_state）
session.cookies['_uuid'] = gen_uuid()
session.cookies['CURRENT_FNVAL'] = "80"
session.cookies['blackside_state'] = "1"

res = session.get(
    url='https://api.bilibili.com/x/web-interface/nav'
)
res.close()
# print(session.cookies.get_dict())

# 3.访问v2，获取sid
aid, bvid, cid, view_count, duration = get_video_info("BV1Mb4y1X73e")
print(aid, bvid, cid, view_count, duration)

res = session.get(
    url="https://api.bilibili.com/x/player/v2",
    params={
        'cid': cid,  # 可以通过一些其他的接口直接获取到
        'aid': aid,
        'bvid': 'BV1Mb4y1X73e',
    }
)
res.close()

# print(session.cookies.get_dict())

# 4.访问click now
res = session.get(
    url="https://api.bilibili.com/x/click-interface/click/now",
    params={
        "jsonp": "jsonp"
    }
)

print(res.text)
