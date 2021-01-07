# -*- coding: utf-8 -*-
# @Author  : WangNing
# @Email   : 3190193395@qq.com
# @File    : DBData_reflect.py
# @Software: PyCharm


class API:
    # api
    api_id = 0
    api_name = 1
    file_name = 2
    req_url = 3
    req_method = 4
    param_type = 5
    has_rely = 6
    status = 7
    create_time = 8


class CASE:
    # case
    id = 0
    api_id = 1
    req_data = 2
    rely_data = 3
    expect_code = 4
    res_data = 5
    check_point = 6
    status = 7
    create_time = 8


class DATA_STORAGE:
    api_id = 0
    case_id = 1
    rely_data = 2
    create_time = 3
