import scrapy


class PostdemoSpider(scrapy.Spider):
    name = 'postDemo'
    allowed_domains = ['www.fy.baidu.com']
    start_urls = ['http://www.fy.baidu.com/']

    def parse(self, response):
        pass
