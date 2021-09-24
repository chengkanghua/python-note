# db.py
import pymysql
from dbutils.pooled_db import PooledDB


class DBHelper(object):

    def __init__(self):
        # TODO 此处配置，可以去配置文件中读取。
        self.pool = PooledDB(
            creator=pymysql,  # 使用链接数据库的模块
            maxconnections=5,  # 连接池允许的最大连接数，0和None表示不限制连接数
            mincached=2,  # 初始化时，链接池中至少创建的空闲的链接，0表示不创建
            maxcached=3,  # 链接池中最多闲置的链接，0和None不限制
            blocking=True,  # 连接池中如果没有可用连接后，是否阻塞等待。True，等待；False，不等待然后报错
            setsession=[],  # 开始会话前执行的命令列表。如：["set datestyle to ...", "set time zone ..."]
            ping=0,
            # ping MySQL服务端，检查是否服务可用。# 如：0 = None = never, 1 = default = whenever it is requested, 2 = when a cursor is created, 4 = when a query is executed, 7 = always
            host='127.0.0.1',
            port=3306,
            user='root',
            password='root123',
            database='userdb',
            charset='utf8'
        )

    def get_conn_cursor(self):
        conn = self.pool.connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        return conn, cursor

    def close_conn_cursor(self, *args):
        for item in args:
            item.close()

    def exec(self, sql, **kwargs):
        conn, cursor = self.get_conn_cursor()

        cursor.execute(sql, kwargs)
        conn.commit()

        self.close_conn_cursor(conn, cursor)

    def fetch_one(self, sql, **kwargs):
        conn, cursor = self.get_conn_cursor()

        cursor.execute(sql, kwargs)
        result = cursor.fetchone()

        self.close_conn_cursor(conn, cursor)
        return result

    def fetch_all(self, sql, **kwargs):
        conn, cursor = self.get_conn_cursor()

        cursor.execute(sql, kwargs)
        result = cursor.fetchall()

        self.close_conn_cursor(conn, cursor)

        return result


db = DBHelper()

