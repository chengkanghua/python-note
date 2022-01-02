import scrapy
from qiubaiPro.items import QiubaiproItem

class QiubaiSpider(scrapy.Spider):
    name = 'qiubai'
    # allowed_domains = ['www.xx.com']
    start_urls = ['https://www.qiushibaike.com/text/']

    url = 'https://www.qiushibaike.com/text/page/%d/'
    page_num = 1
    def parse(self, response):
        div_list = response.xpath('//*[@id="content"]/div/div[2]/div')
        for div in div_list:
            author = div.xpath('./div[1]/a[2]/h2/text()').extract_first()
            content = div.xpath('.//div[@class="content"]/span/text()').extract_first()

            item = QiubaiproItem()
            item['author'] = author
            item['content'] = content

            yield item

        # if self.page_num <= 13:
        #     print('已经爬到第%d页了'%self.page_num)
        #     self.page_num += 1
        #     new_url = format(self.url %self.page_num)
        #     print(new_url)
        #     yield scrapy.Request(url=new_url, callback=self.parse)
