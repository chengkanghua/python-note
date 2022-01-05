#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests
import json
if __name__ == "__main__":
    # URL: https://movie.douban.com/j/chart/top_list?type=24&interval_id=100%3A90&action=&start=20&limit=20
    url = 'https://movie.douban.com/j/chart/top_list'
    param = {
        'type':'24',
        'interval_id':'100:90',
        'action':'',
        'start':'0',
        'limit':'20',
    }

    header = {
        'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }

    response = requests.get(url=url,params=param,headers=header)

    fp = open('./douban.json','w',encoding='utf-8')
    json.dump(obj=response.json(),fp=fp,ensure_ascii=False,indent=2)

