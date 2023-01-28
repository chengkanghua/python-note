from mycelery.main import app
from django_redis import get_redis_connection
from article.models import Article
from datetime import datetime

@app.task(name="write_article")
def write_article():
    """把redis中缓存的文章内容异步写入到MySQL"""
    redis_conn = get_redis_connection("article")
    history_list = redis_conn.keys("article_history_*")
    for user_history_key_bytes in history_list:
        user_history_key = user_history_key_bytes.decode()
        user = int( user_history_key.split("_")[-1] )
        user_history_data_dist = redis_conn.hgetall(user_history_key)
        for article_id_bytes,save_id_bytes in user_history_data_dist.items():
            article_id = article_id_bytes.decode()
            save_id    = save_id_bytes.decode()
            article_dict = redis_conn.hgetall("article_%s_%s_%s" % (user, article_id, save_id) )
            try:
                article = Article.objects.get(pk=article_id)
                article.title = article_dict["title".encode()].decode()
                article.content = article_dict["content".encode()].decode()
                timestamp = datetime.fromtimestamp( int( float( article_dict["updated_time".encode()].decode()) ) )
                article.updated_time = timestamp
                article.save_id = save_id
                article.save()

            except Article.DoesNotExist:
                pass

    # 删除redis中，编辑时间过久的记录
    # 1. 如果编辑记录操作1个月,则删除
    # 2. 如果同一用户编辑记录数量超过100，则最早时间的删除