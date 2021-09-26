import pymysql
from dbutils.pooled_db import PooledDB
from config import settings


class DBHelper:
    def __init__(self):
        self.dbpool = PooledDB(creator=pymysql,**settings.DB_CONFIG)

    def get__conn_cursor(self):
        conn = self.dbpool.connection()
        cursor = conn.cursor(pymysql.cursors.DictCursor)
        return conn, cursor

    def close_conn_cursor(self, *args):
        for item in args:
            item.close()

    def exec(self, sql,*args , **kwargs):
        conn, cursor = self.get__conn_cursor()
        params = args or kwargs
        rows = cursor.execute(sql, params)
        conn.commit()
        self.close_conn_cursor(conn, cursor)
        return rows

    def fetch_one(self, sql, **kwargs):
        conn, cursor = self.get__conn_cursor()
        cursor.execute(sql, kwargs)
        result = cursor.fetchone()
        self.close_conn_cursor(conn, cursor)
        return result

    def fetch_all(self, sql, **kwargs):
        conn, cursor = self.get__conn_cursor()
        cursor.execute(sql, kwargs)
        result = cursor.fetchall()
        self.close_conn_cursor(conn, cursor)
        return result


db = DBHelper()
