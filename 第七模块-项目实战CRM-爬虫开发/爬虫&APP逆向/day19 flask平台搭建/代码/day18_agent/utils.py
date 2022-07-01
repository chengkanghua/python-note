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


def redis_get_task(timeout=10):
    """ redis中获取任务 """
    # 在redis连接池中获取连接，再去做操作
    conn = redis.Redis(connection_pool=REDIS_POOL)

    # 根据连接再去做操作
    data = conn.brpop("YANG_VIDEO_TASK", timeout=timeout)
    if not data:
        return
    return data[-1].decode('utf-8')


def db_update_task_status(oid, status):
    """
    更新订单状态
    :param oid: 订单ID
    :param status:  status=2，正在执行; status=3，执行完成； status=4，执行中断。；
    :return:
    """
    # 获取一个连接
    conn = DB_POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # SQL语句(SQL语句中的sleep)
    sql = "update task set status=%s where oid=%s"
    cursor.execute(sql, [status, oid])
    conn.commit()

    # 将连接交还给数据库连接池
    cursor.close()
    conn.close()


def db_update_task_status_stop(oid, status, exec_count):
    """
    更新订单状态
    :param oid: 订单ID
    :param status:  status=3，执行完成； status=4，执行中断。；
    :param exec_count:  执行次数
    :return:
    """
    # 获取一个连接
    conn = DB_POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # SQL语句(SQL语句中的sleep)
    sql = "update task set status=%s,exec_count=%s where oid=%s"
    cursor.execute(sql, [status, exec_count, oid])
    conn.commit()

    # 将连接交还给数据库连接池
    cursor.close()
    conn.close()


def db_get_task_info(oid):
    """ 获取订单信息：count/URL"""
    conn = DB_POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # SQL语句(SQL语句中的sleep)
    sql = "select * from task where oid=%s"
    cursor.execute(sql, [oid])
    res = cursor.fetchone()

    # 将连接交还给数据库连接池
    cursor.close()
    conn.close()

    return res


def db_retry_stop_task():
    """ 重新执行中断的订单 """

    # 1.获取中断的任务
    conn = DB_POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # SQL语句(SQL语句中的sleep)
    cursor.execute("select * from task where status = 4")
    data_list = cursor.fetchall()

    # 将连接交还给数据库连接池
    cursor.close()
    conn.close()

    # 2.加入队列
    for row_dict in data_list:
        oid = row_dict["oid"]
        redis_push_task(oid)

    # 3.状态更新为待执行
    conn = DB_POOL.connection()
    cursor = conn.cursor(cursor=pymysql.cursors.DictCursor)

    # SQL语句(SQL语句中的sleep)
    cursor.execute("update task set status=1 where status=4")
    conn.commit()

    # 将连接交还给数据库连接池
    cursor.close()
    conn.close()
