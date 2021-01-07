#encoding=utf-8
import unittest, requests
from core.db_manager import *
import os, sys,json

class Users_Login(unittest.TestCase):
    """用户登录"""
    def setUp(self):
        self.dbd = DBManager()
        self.base_url = "http://39.106.41.11:8080/login/"

    def test_users_login_0(self):
        """0"""
        payload = self.dbd.param_completed({'username': 'wcx', 'password': 'wcx123wac'},{'1->1': ['username', 'password']})
        r = requests.post(self.base_url, data = json.dumps(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        
        check_point = {"code": "00","username":{"R":"[a-zA-Z]+"}}
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))


    def tearDown(self):
        self.dbd.close_connect()

