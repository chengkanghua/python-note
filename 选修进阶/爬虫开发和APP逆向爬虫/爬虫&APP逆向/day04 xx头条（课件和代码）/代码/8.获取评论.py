
import requests

res = requests.get(
    url="https://www.toutiao.com/article/v2/tab_comments/?aid=24&app_name=toutiao_web&offset=20&count=20&group_id=7011724095981240835&item_id=7011724095981240835",
    headers={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }
)

print(res.text)
