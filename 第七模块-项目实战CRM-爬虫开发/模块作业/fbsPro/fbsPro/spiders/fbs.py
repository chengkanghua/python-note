import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from fbsPro.items import FbsproItem
from scrapy_redis.spiders import RedisCrawlSpider
class FbsSpider(RedisCrawlSpider):
    name = 'fbs'
    # allowed_domains = ['www.xx.com']
    # start_urls = ['http://www.xx.com/']
    # redis-cli  lpush ershoufang https://bj.58.com/ershoufang/
    redis_key = 'ershoufang'
    link = LinkExtractor(allow=r'ershoufang/p\d+/')
    rules = (
        # Rule(LinkExtractor(allow=r'ershoufang/p\d+/'), callback='parse_item', follow=True),
        Rule(link,callback='parse_item',follow=True),
    )

    def parse_item(self, response):
        div_list = response.xpath('//*[@id="__layout"]/div/section/section[3]/section[1]/section[2]/div')
        for div in div_list:
            title = div.xpath('./a/div[2]/div[1]/div[1]/h3/text()').extract_first()
            price1 = div.xpath('./a/div[2]/div[2]/p[1]/span[1]/text()').extract_first()
            price2 = div.xpath('./a/div[2]/div[2]/p[1]/span[2]/text()').extract_first()
            price = price1+price2
            print(title,price)
            item = FbsproItem()
            item['title'] = title
            item['price'] = price
            yield item
