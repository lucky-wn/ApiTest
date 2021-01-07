# -*- coding: utf-8 -*-
# @Author  : WangNing
# @Email   : 3190193395@qq.com
# @File    : test_db.py
# @Software: PyCharm
from datetime import datetime

import MySQLdb


def test_data():
    conn = MySQLdb.connect(
        host="127.0.0.1",
        port=3306,
        user="root",
        passwd="111111",
        db="api_db",
        charset="utf8"
    )
    cur = conn.cursor()
    conn.select_db('api_db')
    cur.executemany(
        "insert into api(api_name, file_name,r_url, r_method, p_type, rely_db, status, create_time) value(%s,%s,%s,%s,%s,%s,%s,%s)",
        [("用户注册", "user_registration", "http://localhost:8080/register/", "post", "data", 1, 1, datetime.now()),
         ("用户登录", "users_login", "http://localhost:8080/login/", "post", "data", 1, 1, datetime.now())]
        )
    conn.commit()
    cur.executemany(
        "insert into api_case(api_id, req_data,rely_data, expect_code, res_data, check_point, status, create_time) value(%s,%s,%s,%s,%s,%s,%s,%s)",
        [(1, '{"username":"srwcx01","password":"wcx123wac1","email":"wcx@qq.com"}', "", 200,
          '{"request":["username","password"],"response":["code"]}', '{"code":"00"}', 1, datetime.now()),
         (2, "{'username': 'wcx', 'password': 'wcx123wac'}", '{"1->1":["username","password"]}', 200,
          '{"response":["userid", "token"]}', '{"code": "00","username":{"R":"[a-zA-Z]+"}}', 1, datetime.now())
         ]
        )
    conn.commit()
    cur.close()
    conn.close()


if __name__ == "__main__":
    test_data()
