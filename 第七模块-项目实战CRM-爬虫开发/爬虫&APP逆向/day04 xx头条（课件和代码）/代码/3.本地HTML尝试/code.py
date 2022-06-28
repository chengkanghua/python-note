import requests

res = requests.get(
    url="https://www.toutiao.com/api/pc/list/feed?channel_id=3189398957&max_behot_time=1632572648&category=pc_profile_channel&_signature=_02B4Z6wo00f01Tg50AwAAIDAxnWsPKnLkL04EdSAAC9Eed",
    headers={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }
)

print(res.text)
