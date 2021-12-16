import scrapy
from wangyiPro.items import WangyiproItem
from selenium import webdriver

class WangyiSpider(scrapy.Spider):
    name = 'wangyi'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://news.163.com/']
    models_urls = []
    def __init__(self):
        self.bro = webdriver.Chrome(executable_path='/Users/kanghua/PycharmProjects/python-note/第七模块-项目实战CRM-爬虫开发/新版爬虫课程/第七章selenium模块应用/chromedriver')

    def parse(self, response):
        li_list = response.xpath('//*[@id="index2016_wrap"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/ul/li')
        alist = [3,4,6,7,8]
        for index in alist:
            model_url = li_list[index].xpath('./a/@href').extract_first()
            self.models_urls.append(model_url)

        for url in self.models_urls:  # 对每一个板块的url进行请求发送
            yield scrapy.Request(url, callback=self.parse_model)

    def parse_model(self,response):
        div_list = response.xpath('/html/body/div/div[3]/div[4]/div[1]/div/div/ul/li/div/div')
        for div in div_list:
            title = div.xpath('./div/div[1]/h3/a/text()').extract_first()
            new_detail_url = div.xpath('./div/div[1]/h3/a/@href').extract_first()

            item = WangyiproItem()
            item['title'] = title
            yield scrapy.Request(url=new_detail_url,callback=self.parse_detail,meta={'item':item})

    def parse_detail(self, response):  # 解析新闻内容
        content = response.xpath('//*[@id="endText"]//text()').extract()
        content = ''.join(content)
        item = response.meta['item']
        item['content'] = content

        yield item

    def closed(self, spider):
        self.bro.quit()
