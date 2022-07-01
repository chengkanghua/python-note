import pymysql
import random
import datetime
from dbutils.pooled_db import PooledDB
import re
import requests
import redis

# Redis连接池
REDIS_POOL = redis.ConnectionPool(
    host='127.0.0.1', port=6379, password="qwe123", encoding='utf-8', max_connections=100
)

# MySQL数据库连接池
DB_POOL = PooledDB(
    creator=pymysql, maxconnections=10, mincached=2,
    blocking=True, host='127.0.0.1', port=3306, user='root', password='root123', charset="utf8", database='auto'
)


def gen_oid():
    ctime = datetime.datetime.now().strftime("%y%m%d%H%M%S%f")
    rand_num = random.randint(1000, 9999)
    oid = "{}{}".format(ctime, rand_num)
    return oid


def get_old_view_count(url):
    res = requests.get(
        url=url,
        headers={
            'user-agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, '
                          'like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1',
            'referer': 'https://m.yangshipin.cn/',
        }
    )

    match_object = re.findall(r'"subtitle":"(.+)次观看","', res.text)
    if not match_object:
        return 0
    return match_object[0]


def db_create_task(count, video_url, oid):
    """ 下单，在数据库中创建订单 """

    old_count = get_old_view_count(video_url)

    # 获取一个连接
    conn = DB_POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # SQL语句(SQL语句中的sleep)
    sql = "insert into task(oid,old_count,count,url,status) values(%s,%s,%s,%s,%s)"
    cursor.execute(sql, [oid, old_count, count, video_url, 1])
    conn.commit()

    # 将连接交还给数据库连接池
    cursor.close()
    conn.close()


def db_fetch_all_task():
    # 获取一个连接
    conn = DB_POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # SQL语句(SQL语句中的sleep)
    sql = "select * from task order by id desc"
    cursor.execute(sql)
    res = cursor.fetchall()

    # 将连接交还给数据库连接池
    cursor.close()
    conn.close()

    return res


def redis_push_task(oid):
    # 在redis连接池中获取连接，再去做操作
    conn = redis.Redis(connection_pool=REDIS_POOL)

    # 根据连接再去做操作
    conn.lpush("YANG_VIDEO_TASK", oid)
