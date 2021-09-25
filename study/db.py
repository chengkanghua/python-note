import pymysql
from dbutils.pooled_db import PooledDB


class DBHelper:
    def __init__(self):
        self.dbpool = PooledDB(
            creator=pymysql,
            mincached=2,
            maxcached=4,
            maxconnections=5,
            blocking=True,
            setsession=[],
            host='localhost',
            port=3306,
            user='root',
            password='root123',
            database='blogs',
            charset='utf8'
        )

    def get__conn_cursor(self):
        conn = self.dbpool.connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        return conn, cursor

    def close_conn_cursor(self, *args):
        for item in args:
            item.close()
    def exec(self,sql,**kwargs):
        conn,cursor = self.get__conn_cursor()
        cursor.execute(sql,kwargs)
        conn.commit()
        self.close_conn_cursor(conn,cursor)
    def fetch_one(self,sql,**kwargs):
        conn,cursor = self.get__conn_cursor()
        cursor.execute(sql,kwargs)
        result = cursor.fetchone()
        self.close_conn_cursor(conn,cursor)
        return result
    def fetch_all(self,sql,**kwargs):
        conn,cursor = self.get__conn_cursor()
        cursor.execute(sql,kwargs)
        result = cursor.fetchall()
        self.close_conn_cursor(conn,cursor)
        return result


db = DBHelper()