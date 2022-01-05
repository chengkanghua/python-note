import scrapy
from bossPro.items import BossproItem

class BossSpider(scrapy.Spider):
    name = 'boss'
    # allowed_domains = ['www.xxx.com']
    start_urls = ['https://www.zhipin.com/c101010100/?query=python&page=1']
    url = 'https://www.zhipin.com/c101010100/?query=python&page=%s'
    page_num = 1

    def start_requests(self):
        headers = {
            "user-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.121 Safari/537.36',
            "cookie": r'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1639367596; lastCity=100010000; toUrl=https://www.zhipin.com/; __g=-; wd_guid=24b60f69-9cc3-4bc5-a9d2-6e24b1a60466; historyState=state; gdxidpyhxdE=0xIPV4fXa/syuJZMNMEHzmCg166sv41y/MXsOjIiTYeVz28+RpsN4otvuMcgEsz+/IEmKgg7egSG6yTRR6I1rPc2xQyKWMAShD/L9qLamOAEMLEHR\L9fW6zTlUTmQjgdRGfzVg3t\OK/s83+/zhnnz0jfXMHM+Jnw5d2\NfhhgBpUAW:1639381337909; _9755xjdesxxd_=32; YD00951578218230:WM_NI=LaeM0XUMytGJnF0ejpwaVFbUdwXm1LPH1+HkdO0fQhqP2QeE/h3e6mSmbpPaeu/smmSyRo4ZG/i/nNnFr9deXnS/LFGo/feRxZKnAtWaVAjNcgpwF28sDutJDE3mYTBQR3o=; YD00951578218230:WM_NIKE=9ca17ae2e6ffcda170e2e6ee8ece4eb0e8a0d2d96b9bac8fa2d14f928e8aafaa65b8ec968eea5bb5b1a4daf12af0fea7c3b92a90bfabaeb3549793b795c642ae9a0086e97cb5bf9aa7e15fa8a9988eb4489498ffcccb61a8910087d464b390feb2e84fedb8fd86b56791b3ae91d36ba7abe194f06791a79e90b75285f1a7d0ed46ae9abedae76f9cb29dd0cf4e85b1e187e85abc86858fc48095bf9aa2e946a1b9c098c53afcad8c96f742889bfd8edc60828f9ed4ee37e2a3; YD00951578218230:WM_TID=AtOA2PvDDm9FVREQVUY/pp4YzkVlo08v; acw_tc=0bcb2f0116393825805041000e25eb6c328fdfc9383143c3c1c4db6624336e; __c=1639367596; __l=l=/www.zhipin.com/c101010100/?query=python&page=1&r=https://open.weixin.qq.com/&g=&s=3&friend_source=0&s=3&friend_source=0; __a=60096968.1639367596..1639367596.22.1.22.22; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1639382582; __zp_stoken__=9bd6dEC5QXSorBRUUaER3IVxHHRBKLTd4OUcZAW8COWVcbgBTKWxRbg0eDjcNB1NYF0w1XyRrNVlCBmZkFWdiLGs3bF5DQCUYNhExKyMzdy8vK11RGkovTTYic0MsIxw/VXUHdyBDRVwKRxY=; __zp_sseed__=sxsH02GtmlGg0lsUcQKkgbc76v4aZM1kKEuPBZhtuOc=; __zp_sname__=76b2c3fe; __zp_sts__=1639382981376'
         }
        yield scrapy.Request(url=self.start_urls, callback=self.parse, headers=headers)

    def parse_detail(self,response):
        item = response.meta['item']
        job_desc = response.xpath('//*[@id="main"]/div[3]/div/div[2]/div[2]/div[1]/div//text()').extract()
        job_desc = ''.join(job_desc)
        item['job_desc'] = job_desc
        yield item

    # 解析首页岗位名称
    def parse(self, response):
        li_list = response.xpath('//*[@id="main"]/div/div[3]/ul/li')
        print(li_list)
        for li in li_list:
            item = BossproItem()
            job_name = li.xpath('.//span[@class="job_name"]/a/text()').extract_first()
            print(job_name)
            detail_url = 'https://www.zhipin.com'+li.xpath('.//span[@class="job_name"]/a/@href').extract_first()
            print(detail_url)
            yield scrapy.Request(detail_url,callback=self.parse_detail,meta={'item':item})

        if self.page_num <= 3:
            new_url = format(self.url %self.page_num)
            self.page_num += 1

            yield scrapy.Request(new_url,callback=self.parse)


