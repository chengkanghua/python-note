import scrapy
from autohome.items import AutohomeItem

class HomeSpider(scrapy.Spider):
    name = 'home'
    # allowed_domains = ['https://www.autohome.com.cn/all/']
    start_urls = ['https://www.autohome.com.cn/all/1/#liststart']

    url = 'https://www.autohome.com.cn/all/%d/#liststart'
    page_num = 2

    # 回调函数
    def parse_detail(self,response):
        item = response.meta['item']
        title = response.xpath('/html/head/title/text()').extract_first()
        print(title)
        yield item

    # 解析列表页面图片地址
    def parse(self, response):
        li_list = response.xpath('//*[@id="auto-channel-lazyload-article"]/ul[1]/li')
        for li in li_list:
            item = AutohomeItem()
            img_url = li.xpath('a/div[1]/img/@src').extract_first()
            print(img_url)
            item['img_url'] = img_url
            detail_url = "https:%s" % li.xpath('a/@href').extract_first()
            # print(detail_url)
            item['detail_url'] = detail_url
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item['detail_url']})

        # 分页操作
        if self.page_num <= 4:
            new_url = format(self.url%self.page_num)
            self.page_num +=1
            yield scrapy.Request(new_url,callback=self.parse)