# -*- coding: utf-8 -*-
# @Author  : WangNing
# @Email   : 3190193395@qq.com
# @File    : db_tool.py
# @Software: PyCharm
import MySQLdb
import threading
from DBUtils.PooledDB import PooledDB
from common_utils.config_parser import DBConfigParser


class DBPool(object):
    _lock = threading.Lock()

    def __init__(self):

        self.conn = DBPool._instance.connection()
        self.cursor = self.conn.cursor()

    def __new__(cls, *args, **kwargs):
        if not hasattr(DBPool, "_instance"):
            with DBPool._lock:
                if not hasattr(DBPool, "_instance"):
                    cls.conf = DBConfigParser().get_db_config()
                    DBPool._instance = PooledDB(MySQLdb,
                                                maxconnections=15,
                                                blocking=True,
                                                host=cls.conf.get("host"),
                                                user=cls.conf.get("user"),
                                                password=cls.conf.get("password"),
                                                db=cls.conf.get("db_name"),
                                                charset="utf8")
        return object.__new__(cls, *args, **kwargs)

    def get_api_list(self):
        sql = "select * from api where status = 1"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def get_case_list(self, api_id):
        sql = 'select * from api_case where api_id = %s' % api_id
        self.cursor.execute(sql)
        return list(self.cursor.fetchall())

    def close(self):
        self.cursor.close()
        self.conn.close()


if __name__ == '__main__':
    pool = DBPool()
    ret = pool.get_api_list()
    print(ret)
