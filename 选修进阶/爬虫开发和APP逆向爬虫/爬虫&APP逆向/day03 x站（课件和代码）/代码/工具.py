import json

data = 'aid=629890572&cid=318066735&bvid=BV1Mb4y1X73e&part=1&mid=0&lv=0&ftime=1632399715&stime=1632399715&jsonp=jsonp&type=3&sub_type=0&from_spmid=&auto_continued_play=0&refer_url=&bsource=&spmid='
data = 'aid=629890572&cid=318066735&bvid=BV1Mb4y1X73e&mid=0&csrf=&played_time=0&real_played_time=0&realtime=0&start_ts=1632399715&type=3&dt=2&play_type=1&from_spmid=&spmid=&auto_continued_play=0&refer_url=&bsource='
data_dict = {item.split("=")[0]: item.split("=")[1] for item in data.split("&")}

print(json.dumps(data_dict, indent=4))
