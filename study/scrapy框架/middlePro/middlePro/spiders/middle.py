import scrapy


class MiddleSpider(scrapy.Spider):
    name = 'middle'
    # allowed_domains = ['www.xx.com']
    start_urls = ['http://www.baidu.com/s?wd=ip']
    # start_urls = ['https://www.zhipin.com/c101010100/?query=python&page=1']

    def parse(self, response):
        page_text = response.text

        with open('ip.html','w',encoding='utf-8') as fp:
            fp.write(page_text)
