import requests
from lxml import etree
import os
from multiprocessing.dummy import Pool
#需求：爬取梨视频的视频数据

#原则：线程池处理的是阻塞且较为耗时的操作

#对下述url发起请求解析出视频详情页的url和视频的名称
url = 'https://www.pearvideo.com/category_5'
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36'
}
page_text = requests.get(url=url,headers=headers).text

tree = etree.HTML(page_text)
li_list = tree.xpath('//*[@id="categoryList"]/li')

urls_dict = {} #存储所有视频的名字和链接
for li in li_list:
    name = li.xpath('./div/a/div[2]/text()')[0] + '.mp4'
    detail_url = 'https://www.pearvideo.com/'+li.xpath('./div/a/@href')[0]
    urls_dict[name] = detail_url

print(urls_dict)

#从详情页中解析出视频的地址（url）  思路来源 https://www.jb51.net/article/199219.htm
for name,url in urls_dict.items():
    video_id = url.split('/')[-1].split('_')[-1]
    cont_id = f"cont-{video_id}"
    headers = {
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.45 Safari/537.36",
        'Referer': url
    }
    res = requests.get(url=f'https://www.pearvideo.com/videoStatus.jsp?contId={video_id}', headers=headers)
    srcUrl = res.json()['videoInfo']["videos"]['srcUrl']
    srcUrl = srcUrl.replace(srcUrl.split("-")[0].split("/")[-1], cont_id)  #视频的真实地址
    urls_dict[name] = srcUrl

print(urls_dict)

# 创建存储视频目录
if not os.path.exists('./pearvideo'):
    os.mkdir("./pearvideo")

#对视频链接发起请求获取视频的二进制数据，然后将视频数据进行返回
def get_video_data(dic):
    print(dic,'正在下载......')
    data = requests.get(url=urls_dict[dic],headers=headers).content
    #持久化存储操作
    with open(f'./pearvideo/{dic}','wb') as fp:
        fp.write(data)
        print(urls_dict[dic],'下载成功！')

# #使用线程池对视频数据进行请求（较为耗时的阻塞操作）
pool = Pool(4)
pool.map(get_video_data,urls_dict)
pool.close()
pool.join()
