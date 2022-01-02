# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter

import redis,json
class QiubaiproPipeline(object):
    conn = None
    def open_spider(self,spider):
        print('开始爬虫')
        self.conn = redis.Redis(host='127.0.0.1',port=6379)
    def process_item(self,item,spider):
        dict = {
            'author': item['author'],
            'content': item['content']
        }

        self.conn.lpush('data', json.dumps(dict))
        return item


class QiubaiByFiles(object):
    fp = None
    def open_spider(self,spider):
        print('start spider')
        self.fp = open('qiubai.txt','w',encoding='utf-8')
    def process_item(self, item, spider):
        print('已经写入磁盘文件')
        self.fp.write(item['author'].strip()+':'+item['content'].strip()+"\n")
        return item

    def close_spider(self,spider):
        print('over spider')
        self.fp.close()