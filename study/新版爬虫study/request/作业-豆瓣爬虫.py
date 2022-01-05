#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
if __name__ == "__main__":
    # 喜剧排行榜
    # URL: https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=20&limit=20
    url = 'https://movie.douban.com/j/chart/top_list'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    data = []
    for start_num in [0,20]:
        param = {
            'type':'24',
            'interval_id':'100:90',
            'action':'',
            'start':start_num,
            'limit':'20',
        }
        # 免费代理地址 https://www.kuaidaili.com/free/
        response = requests.get(url=url,params=param,headers=header,proxies={"http":"111.160.169.54:41820"})
        data.append(response.json())

fp = open('./douban1.json','a',encoding='utf-8')
json.dump(obj=data,fp=fp,ensure_ascii=False,indent=2)

