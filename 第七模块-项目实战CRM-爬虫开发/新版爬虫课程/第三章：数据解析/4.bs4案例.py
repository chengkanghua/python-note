#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import requests
from bs4 import BeautifulSoup
#需求：爬取三国演义小说所有的章节标题和章节内容http://www.shicimingju.com/book/sanguoyanyi.html
if __name__ == "__main__":
    #对首页的页面数据进行爬取
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36'
    }
    url = 'http://www.shicimingju.com/book/sanguoyanyi.html'
    response = requests.get(url=url,headers=headers)
    # print(response.status_code) # 响应状态code
    # print(response.encoding)  # 打印向前编码
    response.encoding = 'utf-8' # 转码
    page_text = response.text
    print(page_text)

    #在首页中解析出章节的标题和详情页的url
    #1.实例化BeautifulSoup对象，需要将页面源码数据加载到该对象中
    soup = BeautifulSoup(page_text,'lxml')
    #解析章节标题和详情页的url
    li_list = soup.select('.book-mulu > ul > li')
    fp = open('./sanguo.txt','w',encoding='utf-8')
    for li in li_list:
        title = li.a.string
        detail_url = 'http://www.shicimingju.com'+li.a['href']
        #对详情页发起请求，解析出章节内容
        response = requests.get(url=detail_url,headers=headers)
        response.encoding = 'utf-8'
        detail_page_text = response.text
        #解析出详情页中相关的章节内容
        detail_soup = BeautifulSoup(detail_page_text,'lxml')
        div_tag = detail_soup.find('div',class_='chapter_content')
        #解析到了章节的内容
        content = div_tag.text
        fp.write(title+':'+content+'\n')
        print(title,'爬取成功！！！')


