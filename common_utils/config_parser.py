# -*- coding: utf-8 -*-
# @Author  : WangNing
# @Email   : 3190193395@qq.com
# @File    : config_parser.py
# @Software: PyCharm
import configparser
from variables.static_variables import DB_CONFIG


class DBConfigParser:
    """
    读取数据库配置文件中的连接参数
    """

    def __init__(self):
        self.parser = configparser.ConfigParser()

    def get_db_config(self):
        self.parser.read(DB_CONFIG)
        host = self.parser.get("mysql_db", "host")
        port = self.parser.get("mysql_db", "port")
        db_name = self.parser.get("mysql_db", "db_name")
        user = self.parser.get("mysql_db", "user")
        password = self.parser.get("mysql_db", "password")
        return {"host": host, "port": port, "db_name": db_name, "user": user, "password": password}


if __name__ == '__main__':
    ret = DBConfigParser().get_db_config()
    print(ret)