import os
import subprocess
import requests

os.environ["NODE_PATH"] = "/usr/local/lib/node_modules/"
# 1.编译（报错：缺少window、document等浏览器必备的环境）
# 2.执行 window.byted_acrawler.sign({url:url})

url = "https://www.toutiao.com/api/pc/list/feed?offset=0&channel_id=3189398957&max_behot_time=0&category=pc_profile_channel"
signature = subprocess.getoutput('node acrawler.js "{}"'.format(url))
signature = signature.strip()
finally_url = "{}&_signature={}".format(url, signature)

res = requests.get(
    url=finally_url,
    headers={
        "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
    }
)

print(res.text)
