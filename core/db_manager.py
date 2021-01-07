# -*- coding: utf-8 -*-
# @Author  : WangNing
# @Email   : 3190193395@qq.com
# @File    : db_manage.py
# @Software: PyCharm
import json
from datetime import datetime

import MySQLdb

from common_utils.config_parser import DBConfigParser
from common_utils.md5_tool import md5_encrypt


class DBManager(object):
    def __init__(self):
        self.db_config = DBConfigParser()
        config = self.db_config.get_db_config()
        self.conn = MySQLdb.connect(
            host=config["host"],
            user=config["user"],
            passwd=config["password"],
            db=config["db_name"],
            charset="utf8"
        )
        # 设置数据库变更自动提交
        self.conn.autocommit(1)
        self.cursor = self.conn.cursor()

    def close_connect(self):
        self.conn.commit()
        self.cursor.close()
        self.conn.close()

    def param_completed(self, param, rely_data):
        """
        处理依赖数据，请求参数化
        :param param:
        :param rely_data:
        :return:
        """
        param_source = param.copy()
        for key, value in rely_data.items():
            api_id, case_id = key.split("->")
            rely_data = json.loads(self.get_rely_data(int(api_id), int(case_id)))
            for k, v in rely_data.items():
                if k in param_source.keys():
                    param_source[k] = v
        return param_source

    def write_in_store_data(self, api_id, case_id, storeData):
        has_rely_data = self.has_rely_data(api_id, case_id)
        if has_rely_data:
            sql = "update data_storage set data_store = \'%s\', ctime = \"%s\"  where api_id = %s and case_id = %s"\
                  % (storeData, datetime.now(), api_id, case_id)
            return self.cursor.execute(sql)
        else:
            sql = "insert into data_storage values (%s, %s, \'%s\', \"%s\")" % (
                api_id, case_id, storeData, datetime.now())
            print(sql)
            res = self.cursor.execute(sql)
            return res

    def store_data(self, api_id, case_id, storeReg, requestData=None, responseData=None):
        store_data = {}
        for key, value in storeReg.items():
            if requestData and key == 'request':
                for i in value:
                    if i in requestData.keys():
                        if i == 'password':
                            store_data[i] = md5_encrypt(requestData[i])
                        else:
                            store_data[i] = requestData[i]
            elif responseData and key == 'response':
                for j in value:
                    if j in responseData.keys():
                        if j == 'password':
                            store_data[j] = md5_encrypt(responseData[j])
                        else:
                            store_data[j] = responseData[j]
        # 写入数据库
        self.write_in_store_data(api_id, case_id, store_data)

    def has_rely_data(self, api_id, case_id):
        """
        判断是否有依赖数据
        :param api_id:
        :param case_id:
        :return:
        """
        sql = "select data_store from data_storage where api_id = %s and case_id = %s" % (api_id, case_id)
        # 返回受影响条目数，0表示没查到
        return self.cursor.execute(sql)

    def get_rely_data(self, api_id, case_id):
        """
        获取依赖数据
        :param api_id:
        :param case_id:
        :return:
        """
        sql = "select rely_data from data_storage where api_id = %s and case_id = %s" % (api_id, case_id)
        result = self.cursor.execute(sql)
        if result == 0:
            return False
        else:
            return self.cursor.fetchall()[0][0]
