import scrapy


class XiaohuaSpider(scrapy.Spider):
    name = 'xiaohua'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://nice.ruyile.com/?f=3&p=1']
    #生成一个通用的url模板(不可变)
    url = 'https://nice.ruyile.com/?f=3&p=%s'
    page_num = 1
    def parse(self, response):
        '''
        需求：爬取校花网中的照片的名称
        :param response:
        :return:
        '''
        # div_list = response.xpath('//*[@class="m3_xhtp"]/div')
        div_list = response.xpath('//*[@class="m3_xhtp"]/div[@class="tp_list"]')
        # print(div_list)
        for div in div_list:
            img_name = div.xpath('./div[2]/a/text()').extract_first()
            print(img_name)
        if self.page_num <= 5:
            new_url = format(self.url %self.page_num)
            self.page_num += 1
            yield scrapy.Request(url=new_url,callback=self.parse)