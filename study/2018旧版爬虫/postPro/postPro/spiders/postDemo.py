import scrapy


class PostdemoSpider(scrapy.Spider):
    name = 'postDemo'
    # allowed_domains = ['www.fanyi.baidu.com']
    start_urls = ['https://fanyi.baidu.com/sug']
    def start_requests(self):
        word = input('请输入想查询的单词:')
        data = {
            'kw': word,
        }
        for url in self.start_urls:
            yield scrapy.FormRequest(url=url,formdata=data, callback=self.parse)

    def parse(self, response):
        # print(response.text.encode('latin-1').decode('unicode_escape'))
        print(response.text.encode('latin-1').decode('unicode_escape'))