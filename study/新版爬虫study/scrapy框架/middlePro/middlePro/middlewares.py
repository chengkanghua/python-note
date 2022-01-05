# Define here the models for your spider middleware
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
import random
# useful for handling different item types with a single interface
from itemadapter import is_item, ItemAdapter


class MiddleproDownloaderMiddleware:
    # Not all methods need to be defined. If a method is not defined,
    # scrapy acts as if the downloader middleware does not modify the
    # passed objects.
    user_agent_list = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1",
        "Mozilla/5.0 (X11; CrOS i686 2268.111.0) AppleWebKit/536.11 "
        "(KHTML, like Gecko) Chrome/20.0.1132.57 Safari/536.11",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1092.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.6 "
        "(KHTML, like Gecko) Chrome/20.0.1090.0 Safari/536.6",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/537.1 "
        "(KHTML, like Gecko) Chrome/19.77.34.5 Safari/537.1",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.9 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.0) AppleWebKit/536.5 "
        "(KHTML, like Gecko) Chrome/19.0.1084.36 Safari/536.5",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 5.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_0) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1063.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1062.0 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.1 Safari/536.3",
        "Mozilla/5.0 (Windows NT 6.2) AppleWebKit/536.3 "
        "(KHTML, like Gecko) Chrome/19.0.1061.0 Safari/536.3",
        "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24",
        "Mozilla/5.0 (Windows NT 6.2; WOW64) AppleWebKit/535.24 "
        "(KHTML, like Gecko) Chrome/19.0.1055.1 Safari/535.24"
    ]
    PROXY_http = [
        '153.180.102.104:80',
        '195.208.131.189:56055',
    ]
    PROXY_https = [
        '120.83.49.90:9000',
        '95.189.112.214:35508',
    ]
    @classmethod
    def from_crawler(cls, crawler):
        # This method is used by Scrapy to create your spiders.
        s = cls()
        crawler.signals.connect(s.spider_opened, signal=signals.spider_opened)
        return s

    # 请求处理
    def process_request(self, request, spider):
        # request.headers['User-Agent'] = random.choice(self.user_agent_list)
        request.headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.45 Safari/537.36 Edg/97.0.1072.34'
        # request.headers['Cookie'] = r'Hm_lvt_194df3105ad7148dcf2b98a91b5e727a=1639367596; lastCity=100010000; toUrl=https://www.zhipin.com/; __g=-; wd_guid=24b60f69-9cc3-4bc5-a9d2-6e24b1a60466; historyState=state; gdxidpyhxdE=0xIPV4fXa/syuJZMNMEHzmCg166sv41y/MXsOjIiTYeVz28+RpsN4otvuMcgEsz+/IEmKgg7egSG6yTRR6I1rPc2xQyKWMAShD/L9qLamOAEMLEHR\L9fW6zTlUTmQjgdRGfzVg3t\OK/s83+/zhnnz0jfXMHM+Jnw5d2\NfhhgBpUAW:1639381337909; _9755xjdesxxd_=32; YD00951578218230:WM_NI=LaeM0XUMytGJnF0ejpwaVFbUdwXm1LPH1+HkdO0fQhqP2QeE/h3e6mSmbpPaeu/smmSyRo4ZG/i/nNnFr9deXnS/LFGo/feRxZKnAtWaVAjNcgpwF28sDutJDE3mYTBQR3o=; YD00951578218230:WM_NIKE=9ca17ae2e6ffcda170e2e6ee8ece4eb0e8a0d2d96b9bac8fa2d14f928e8aafaa65b8ec968eea5bb5b1a4daf12af0fea7c3b92a90bfabaeb3549793b795c642ae9a0086e97cb5bf9aa7e15fa8a9988eb4489498ffcccb61a8910087d464b390feb2e84fedb8fd86b56791b3ae91d36ba7abe194f06791a79e90b75285f1a7d0ed46ae9abedae76f9cb29dd0cf4e85b1e187e85abc86858fc48095bf9aa2e946a1b9c098c53afcad8c96f742889bfd8edc60828f9ed4ee37e2a3; YD00951578218230:WM_TID=AtOA2PvDDm9FVREQVUY/pp4YzkVlo08v; acw_tc=0bdd34ca16394696181581850e019c22dc29c8b1a15e70983aabcf9c7beec7; __c=1639367596; __l=l=/www.zhipin.com/c101010100/?query=python&page=1&r=https://open.weixin.qq.com/&g=&s=3&friend_source=0&s=3&friend_source=0; __a=60096968.1639367596..1639367596.24.1.24.24; __zp_stoken__=5fb9dPC4BVT4sFAZZHhleWGg/MTgzFzYuOlh7XSwSWUVJPGJBd1BcK29YMmI0CG9NNi4JcyRLX39HH3UVUxtiWyZrAmUnfDcuI1paWnBSTVt4SU1UTlwTTEBwCyc/JgkGdBc7WyA/XQN4BXQ=; Hm_lpvt_194df3105ad7148dcf2b98a91b5e727a=1639469620'

        # request.meta['proxy'] = 'http://47.243.190.108:7890'
        return None
    # 响应处理
    def process_response(self, request, response, spider):
        # Called with the response returned from the downloader.

        # Must either;
        # - return a Response object
        # - return a Request object
        # - or raise IgnoreRequest
        return response
    # 异常处理
    def process_exception(self, request, exception, spider):
        # Called when a download handler or a process_request()
        # (from other downloader middleware) raises an exception.

        # Must either:
        # - return None: continue processing this exception
        # - return a Response object: stops process_exception() chain
        # - return a Request object: stops process_exception() chain
        pass

    def spider_opened(self, spider):
        spider.logger.info('Spider opened: %s' % spider.name)
