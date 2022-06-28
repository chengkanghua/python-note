import requests

res = requests.get(
    url="https://www.toutiao.com/api/pc/list/feed?channel_id=0&category=pc_profile_recommend&need_top=false&max_behot_time=1632580393&_signature=_02B4Z6wo00d0140NYaQAAIDCc0EdlPjDt.eNKWUAAIIUCxFIRv3ALE2XpZIM7J1a22tAMU4Qqmirr8x.xLJQ8SU6KaHGe6QAfgSt2BLRuJ95zzNnl.ZayN8YtXdDzm3fiq0aZEDMzaf.pqLs1c",
    headers={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }
)

print(res.text)
