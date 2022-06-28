import os
import json
import requests
import subprocess
from base64 import b64decode
from urllib.parse import urlencode

import execjs


def get_signature(url):
    # /usr/local/lib/node_modules/jsdom
    os.environ["NODE_PATH"] = "/usr/local/lib/node_modules/"
    signature = subprocess.getoutput('node acrawler.js "{}"'.format(url))
    return signature.strip()


def get_signature_execjs(url):
    os.environ["NODE_PATH"] = "/usr/local/lib/node_modules/"
    with open('acrawler.js', mode='r', encoding='utf-8') as f:
        js = f.read()
    js_compile = execjs.compile(js)

    sign = js_compile.call("get_sign", url)
    return sign


def run():
    base_url = "https://www.toutiao.com/api/pc/list/feed"

    params = {
        "offset": 32,
        "channel_id": "94349549395",
        "max_behot_time": "0",
        "category": "pc_profile_channel",
    }
    url = "{}?{}".format(base_url, urlencode(params))

    # sign = get_signature(url)
    sign = get_signature_execjs(url)
    print(sign)

    params['_signature'] = sign

    res = requests.get(
        url=base_url,
        params=params,
        headers={
            'user-agent': "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.82 Safari/537.36"
        }
    )

    data_list = res.json()['data']
    for item in data_list:
        raw_data = item['raw_data']
        data_string = b64decode(raw_data).decode('utf-8')
        row_dict = json.loads(data_string)
        print(row_dict)
        print('------')


if __name__ == '__main__':
    run()
