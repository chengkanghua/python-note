import requests
from lxml import etree

url = 'https://www.zhipin.com/c101010100/?query=python&page=1'
header = {
    'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.36 Safari/537.36 Edg/97.0.1072.28',
    # 'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'Cookie':'__g=-; Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1639367596; lastCity=100010000; acw_tc=0bdd34ca16393724403827588e01a0aa87e01ea95e4bccc7a73e0021e5a0d1; __c=1639367596; __l=l=/www.zhipin.com/c101010100/?query=python&page=4&r=&g=&s=3&friend_source=0&s=3&friend_source=0; __a=60096968.1639367596..1639367596.13.1.13.13; __zp_stoken__=9bd6dEC5QXSoranYDQg05IVxHHRAzU0ZaGUcZAW8COWUyVQFgYmxRbg0eVRtbAllwF0w1XyRrL1k1A2pkHFxXPC4SWk4sEDs5QBI6KyMzdy8vK3VbHxwDFjYic0MsaBw/VXUHdyBDRVwKRxY=; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1639372654; __zp_sseed__=sxsH02GtmlGg0lsUcQKkgSmNEsMOibs5oYH8rdeh4us=; __zp_sname__=76b2c3fe; __zp_sts__=1639372660409',
}

page_text = requests.get(url=url,headers=header).text
fp = open('boss.html','w',encoding='utf-8')
fp.write(page_text)
fp.close()
tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="main"]/div/div[3]/ul/li') 
print(li_list)
# for li in li_list:
#     job_name = li.xpath('.//span[@class="job_name"]/a/text()')
#     print(job_name)


