# -*- coding: utf-8 -*-
# @Author  : WangNing
# @Email   : 3190193395@qq.com
# @File    : static_variables.py
# @Software: PyCharm

import os

# 工程目录
PROJECT_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 数据库配置文件
DB_CONFIG = PROJECT_PATH + "/config/db_config.ini"
# 测试脚本存放位置
SCRIPT_PATH = PROJECT_PATH + "/scripts"

if __name__ == '__main__':
    print(PROJECT_PATH)
    print(SCRIPT_PATH)
    print(DB_CONFIG)
