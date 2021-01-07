# -*- coding: utf-8 -*-
# @Author  : WangNing
# @Email   : 3190193395@qq.com
# @File    : script_variables.py
# @Software: PyCharm

# 生成脚本时，相关变量的存储
# 脚本预备：导入包
code_prepares = """#encoding=utf-8
import unittest, requests
from core.db_manager import *
import os, sys,json"""
# 脚本头部[需要连接数据库(有依赖数据)]：class, setup
code_head_with_db = '''
class %s(unittest.TestCase):
    """%s"""
    def setUp(self):
        self.dbd = DBManager()
        self.base_url = "%s"
'''
# 脚本头部[不需要连接数据库]：class, setup
code_head = '''
class %s(unittest.TestCase):
    """%s"""
    def setUp(self):
        self.base_url = "%s"
'''
# 脚本结束
code_end = """
"""
# 脚本结束（带数据库连接）
code_end_with_db = """
    def tearDown(self):
        self.dbd.close_connect()
"""
# 结束
final_code = '''
if __name__ == '__main__':
    unittest.main()
'''
# post方法
post_code = '''
    def test_%s(self):
        """%s"""
        %s
        r = requests.post(self.base_url, data = json.dumps(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        %s
'''
# get方法
get_code = '''\n
    def test_%s(self):
        """%s"""
        %s
        r = requests.get(self.base_url + str(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        %s
'''
# 校验
check_code = '''
        check_point = %s
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))
'''
