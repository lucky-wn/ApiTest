# -*- coding: utf-8 -*-
# @Author  : WangNing
# @Email   : 3190193395@qq.com
# @File    : main_enter.py
# @Software: PyCharm

import sys
from datetime import datetime

from unittest import defaultTestLoader
from common_utils import HTMLTestRunner
from core.script_creator import make_script

sys.path.append("./script")

if __name__ == '__main__':
    make_script()
    now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    test_dir = "../scripts"
    discover = defaultTestLoader.discover(test_dir, pattern="*_test.py", top_level_dir=None)
    filename = "../report/" + now + "_result.html"
    with open(filename, "wb") as file:
        runner = HTMLTestRunner.HTMLTestRunner(
            stream=file,
            title=u'自动化测试报告',
            description='测试用例结果',  # 不传默认为空
            # tester=u"wang"  # 测试人员名字，不传默认为QA
        )
        runner.run(discover)
