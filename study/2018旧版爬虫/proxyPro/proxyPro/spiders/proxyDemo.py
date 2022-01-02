import scrapy


class ProxydemoSpider(scrapy.Spider):
    name = 'proxyDemo'
    # allowed_domains = ['www.baidu.com']
    start_urls = ['https://www.baidu.com/s?wd=ip']

    def parse(self, response):
        with open('baidu.html','w',encoding='utf-8') as fp:
            fp.write(response.text)
