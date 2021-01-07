# -*- coding: utf-8 -*-
# @Author  : WangNing
# @Email   : 3190193395@qq.com
# @File    : md5_tool.py
# @Software: PyCharm

import hashlib


def md5_encrypt(text):
    """
    md5加密
    """
    md = hashlib.md5()
    md.update(text)
    return md.hexdigest()


if __name__ == '__main__':
    print(md5_encrypt("你好".encode("utf-8")))
