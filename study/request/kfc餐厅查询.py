import requests,json
if __name__ == '__main__':
    url = 'http://www.kfc.com.cn/kfccda/ashx/GetStoreList.ashx?op=keyword'
    header = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.55 Safari/537.36 Edg/96.0.1054.34'
    }
    search_city = input('请输入查询地区： ')
    result_list = []
    for page_num in range(1,11):
        param = {
            "cname":"",
            "pid":"",
            "keyword":search_city,
            "pageIndex" : page_num,
            "pageSize": "10",
        }


        response = requests.post(url=url,params=param,headers=header)
        # print(response.json())
        # print(type(response.json()))  # dict类型
        result_list.append(response.json()['Table1'])

    print(result_list)

    fp = open(search_city+'.json','w',encoding='utf-8')
    json.dump(obj=result_list,fp=fp,ensure_ascii=False,indent=2)

