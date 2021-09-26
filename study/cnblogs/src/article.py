import datetime
from utils.context import ArticleModel, UpDownModel
from utils.db_pool import db


class Article(object):
    # 发布文章
    def publish(self, title, text, user_id):
        sql = 'insert into article(title,text,user_id,ctime) values(%s,%s,%s,%s)'
        result = db.exec(sql, title, text, user_id, datetime.datetime.now())
        return result

    # 文章总数
    @property
    def article_count(self):
        sql = 'select count(1) from article'
        result = db.fetch_one(sql)
        return result

    # 文章列表
    def article_list(self, limit, offset):
        sql = 'select title,text from article order by id asc limit %s offset %s'
        result = db.fetch_all(sql, limit, offset)
        return result

    # 文章详情
    def get_article(self, article_id):
        sql = 'select {} from article where id=%s'.format(ArticleModel.db_fields())
        result = db.fetch_one(sql, article_id)
        if not result:
            return None
        return ArticleModel(result)  # 数据存到对象里了

    # 获取踩赞记录情况
    def get_up_down(self, user_id):
        sql = 'select id,choice from up_down where id=%s '
        result = db.fetch_one(sql, user_id)
        if not result:
            return None
        return UpDownModel(result)  # 数据存到对象里了

    # 踩
    def setp(self, user_id, article_id):
        sql = 'insert into up_down(choice,user_id,article_id,ctime) values(%s,%s,%s,%s)'
        db.exec(sql, 0, user_id, article_id, datetime.datetime.now())

        step_sql = 'update article set step_count=step_count+1 where id = %s'
        db.exec(step_sql, article_id)
        return True

    # 赞
    def support(self, user_id, article_id):
        sql = 'insert into up_down(choice,user_id,article_id,ctime) values(%s,%s,%s,%s)'
        db.exec(sql, 1, user_id, article_id, datetime.datetime.now())

        up_sql = 'update article set support_count=support_count+1 where id=%s'
        db.exec(up_sql, article_id)

        return True

    # 更新文章阅读数
    def update_read(self, article_id):
        sql = 'update article set read_count=read_count+1 where id=%s'
        result = db.exec(sql, article_id)
        return result

    # 更新踩到赞
    def update_step(self, user_id, article_id):
        sql = 'update up_down set choice=1 where user_id=%s and article_id=%s'
        db.exec(sql, user_id, article_id)

        step_sql = 'update article set step_count=step_count-1,support_count=support+1 where id=%s'
        db.exec(step_sql, article_id)
        return True

    # 更新赞到踩
    def update_support(self, user_id, article_id):
        sql = 'update up_down set choice=0 where user_id=%s and article_id=%s'
        db.exec(sql, user_id, article_id)

        step_sql = 'update article set step_count=step_count+1,support_count=support-1 where id=%s'
        db.exec(step_sql, article_id)
        return True

    # 评论
    def comment(self, content, user_id, article_id):
        sql = 'insert into comment(content,user_id,article_id,ctime)'
        result = db.exec(sql, content, user_id, article_id, datetime.datetime.now())
        return result


art = Article()

if __name__ == '__main__':
    art = Article()
    art.get_article(1)
