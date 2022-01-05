import requests,os
from lxml import etree

url = 'https://sc.chinaz.com/jianli/free_%s.html'
headers = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
}

# url集合
url_list = ['https://sc.chinaz.com/jianli/free.html',]
for i in range(2,30):
    url_list.append(url %i)

# print(url_list)
detail_url_list = []
download_url_list = []

# 下载详情页集合
for site_url in url_list:
    page_text = requests.get(url=site_url,headers=headers).text
    tree  = etree.HTML(page_text)
    a_list = tree.xpath('//*[@id="container"]/div/a')
    for a in a_list:
        detail_url_list.append(a.xpath('./@href')[0])

print(detail_url_list)

# 下载地址集合
for detail_url in detail_url_list:
    page_text = requests.get(url='https:%s' %detail_url,headers=headers).text
    tree = etree.HTML(page_text)
    download_url = tree.xpath('//*[@id="down"]/div[2]/ul/li[1]/a/@href')[0]
    download_url_list.append(download_url)

print(download_url_list) # ['//sc.chinaz.com/jianli/211203121040.htm',....]

# 下载文件
if not os.path.exists('./jianlifile'):
    os.mkdir('./jianlifile')
for download_url in download_url_list:
    file_name = download_url.split('/')[-1]
    file_obj = requests.get(url=download_url,headers=headers).content
    fp = open('./jianlifile/%s' %file_name,'wb')
    fp.write(file_obj)
    fp.close()

print('over')

