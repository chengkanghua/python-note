import scrapy
from imgsPro.items import ImgsproItem

class ImgSpider(scrapy.Spider):
    name = 'img'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://sc.chinaz.com/tupian/']

    def parse(self, response):
        div_list = response.xpath('//div[@id="container"]/div')
        print(div_list)
        for div in div_list:
            src = "https:"+ div.xpath('./div/a/img/@src2').extract_first()
            print(src)
            item = ImgsproItem()
            item['src'] = src
            yield item
