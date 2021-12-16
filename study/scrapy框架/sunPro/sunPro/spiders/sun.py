import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule
from sunPro.items import SunproItem,DetailItem

class SunSpider(CrawlSpider):
    name = 'sun'
    # allowed_domains = ['www.xx.com']
    start_urls = ['https://wz.sun0769.com/political/index/politicsNewest']
    # 链接提取器：根据指定规则（allow="正则"）进行指定链接的提取
    link = LinkExtractor(allow=r'id=1&page=\d+')
    link_detail = LinkExtractor(allow=r'political/politics/index?id=\d+')
    rules = (
        Rule(link,callback='parse_item',follow=True),
        Rule(link_detail,callback='parse_detail')
    )
    # 解析新闻编号和新闻的标题
    def parse_item(self, response):
        li_list = response.xpath('/html/body/div[2]/div[3]/ul[2]/li')
        for li in li_list:
            new_num = li.xpath('./span[1]/text()').extract_first()
            new_title = li.xpath('./span[3]/a/text()').extract_first()
            item = SunproItem()
            item['title'] = new_title
            item['new_num'] = new_num

            yield item
    # 解析新闻内容和新闻编号
    def parse_detail(self,response):
        new_id = response.xpath('/html/body/div[3]/div[2]/div[2]/div[1]/span[4]/text()').extract_first()
        new_content = response.xpath('/html/body/div[3]/div[2]/div[2]/div[2]/pre/text()').extract()
        new_content = ''.join(new_content)
        item = DetailItem()
        item['new_id'] = new_id
        item['new_content'] = new_content
        
        yield item
