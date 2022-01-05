# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pymysql

class QiubaiproPipeline:
    fp = None
    # 重写父类方法, 开始爬虫时候调用
    def open_spider(self,spider):
        print('开始爬虫...')
        self.fp = open('./qiubai.txt','w',encoding='utf-8')
    def process_item(self, item, spider):
        author = item['author']
        content = item['content']
        self.fp.write(author+":"+content+"\n")
        return item  # 会传递给下一个即将执行的管道类

    def close_spider(self,spider):
        print('结束爬虫')
        self.fp.close()

class mysqlPipeline(object):
    conn = None
    cursor = None
    def open_spider(self,spider):
        self.conn = pymysql.Connect(host='127.0.0.1',port=3306,user='root',password='root123',db='qiubai',charset='utf8')

    def process_item(self,item,spider):
        '''
        提前创建好数据库
        create database qiubai charset utf8 collate utf8_general_ci;
        use qiubai;
        CREATE TABLE `qiubai` (
          `author` varchar(100) DEFAULT NULL,
          `content` varchar(9999) DEFAULT NULL
        ) ENGINE=InnoDB DEFAULT CHARSET=utf8
        :param spider:
        :return:
        '''
        self.cursor = self.conn.cursor()
        try:
            self.cursor.execute('insert into qiubai values("%s","%s")' %(item['author'],item['content']))
            self.conn.commit()
        except Exception as e:
            print(e)
            self.conn.rollback()
        return item

    def close_spider(self,spider):
        self.cursor.close()
        self.conn.close()


