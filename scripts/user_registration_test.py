#encoding=utf-8
import unittest, requests
from core.db_manager import *
import os, sys,json

class User_Registration(unittest.TestCase):
    """用户注册"""
    def setUp(self):
        self.dbd = DBManager()
        self.base_url = "http://39.106.41.11:8080/register/"

    def test_user_registration_0(self):
        """0"""
        payload = {"username":"sssrwcx01","password":"wcx123wac1","email":"wcx@qq.com"} 
        r = requests.post(self.base_url, data = json.dumps(payload))
        result = r.json()
        self.assertEqual(r.status_code, 200)
        
        check_point = {"code":"00"}
        for key,value in check_point.items():
            self.assertEqual(result[key], value, msg = u"字段【{}】: expection: {}, reality: {}".format(key, value, result[key]))


    def tearDown(self):
        self.dbd.close_connect()

