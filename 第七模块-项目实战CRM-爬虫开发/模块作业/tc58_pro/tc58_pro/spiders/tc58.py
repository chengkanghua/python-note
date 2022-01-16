import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from tc58_pro.items import Tc58ProItem

class Tc58Spider(CrawlSpider):
    name = 'tc58'
    allowed_domains = ['www.xx.com']
    # start_urls = ['https://bj.58.com/ershoufang/']
    start_urls = ['https://www.autohome.com.cn/all/']
    # link = LinkExtractor(allow=r'/ershoufang/p\d+/')
    link = LinkExtractor(allow=r'/all/\d+/#liststart')
    rules = (
        Rule(link, callback='parse_item', follow=True),
    )

    def parse_item(self, response):
        print(response)
