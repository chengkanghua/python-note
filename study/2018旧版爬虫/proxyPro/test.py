import requests
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.45 Safari/537.36 Edg/97.0.1072.34'
}
url = 'http://www.baidu.com/s?wd=ip'

response = requests.get(url=url,headers=headers,proxies={'http':'139.217.101.57:9080'})
fp = open('bb.html','w',encoding='utf-8')
fp.write(response.text)
fp.close()

