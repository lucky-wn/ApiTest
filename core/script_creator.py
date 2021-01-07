# -*- coding: utf-8 -*-
# @Author  : WangNing
# @Email   : 3190193395@qq.com
# @File    : script_creator.py
# @Software: PyCharm
from common_utils.db_tool import DBPool
from variables.static_variables import SCRIPT_PATH
from variables.DBData_reflect import *
from variables.script_variables import *


def make_script():
    """
    生成测试脚本
    :return:
    """
    db = DBPool()
    api_list = db.get_api_list()
    for api in api_list:
        case_list = db.get_case_list(api[API.api_id])
        create_file(api, case_list)


def create_file(api, case_list):
    with open(SCRIPT_PATH + "\\" + api[API.file_name] + "_test.py", "w", encoding='utf8') as fp:
        fp.write(code_prepares + "\n")
        if api[API.has_rely] == 1:
            # 此api有依赖数据
            fp.write(code_head_with_db % (api[API.file_name].title(), api[API.api_name], api[API.req_url]))
        else:
            fp.write(code_head % (api[API.file_name].title(), api[API.api_name], api[API.req_url]))
        param_code = ""
        for index, case in enumerate(case_list):
            if case[CASE.rely_data]:
                # 具有依赖数据
                param_code = """payload = self.dbd.param_completed(%s,%s)""" % (eval(case[CASE.req_data]), eval(case[CASE.rely_data]))
            else:
                # 不需要一来数据
                param_code = """payload = %s """ % case[CASE.req_data]
            store_data = ""
            if case[CASE.res_data]:
                # 需要向数据库写入存储依赖数据
                store_data = """self.dbd.store_data(%s, %s, %s, %s, %s)""" % (
                    int(case[CASE.api_id]), int(case[CASE.id]), case[CASE.req_data],
                    case[CASE.res_data] if case[CASE.req_data] else None, "result")
            store_code = ""
            if case[CASE.check_point]:
                store_code += check_code % case[CASE.check_point]
            if api[API.req_method] == "post":
                fp.write(post_code % (api[API.file_name] + "_" + str(index), str(index), param_code, store_code))
            elif api[API.req_method] == "get":
                fp.write(get_code % (api[API.file_name] + "_" + str(index), str(index), param_code, store_code))
        if api[API.has_rely] == 1:
            fp.write(code_end_with_db)
        fp.write(code_end)
        fp.close()
