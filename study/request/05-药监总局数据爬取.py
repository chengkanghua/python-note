#!/usr/bin/env python
# -*- coding:utf-8 -*-
import requests,json

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}
url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
id_list = []   # 企业id
info_list = []  # 企业详细信息
for page_num in range(1,6):
    parms = {
        "on": "true",
        "page": page_num,
        "pageSize": "15",
        "productName": "",
        "conditionType": "1",
        "applyname":"" ,
        "applysn": "",
        }
    response = requests.post(url=url,data=parms,headers=headers).json()
    for dic in response['list']:
        id_list.append(dic['ID'])

print(id_list)

post_url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
for ID in id_list:
    parms = {
        "id": ID
    }
    response = requests.post(url=post_url,data=parms,headers=headers).json()
    info_list.append(response)

print(info_list)

fp = open('allData.json','w',encoding='utf-8')
json.dump(obj=info_list,fp=fp,ensure_ascii=False,indent=2)