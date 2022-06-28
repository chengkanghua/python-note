
import requests

res = requests.get(
    url="https://www.toutiao.com/api/pc/list/feed?offset=25&channel_id=94349549395&max_behot_time=0&category=pc_profile_channel",
    headers={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }
)

print(res.text)
