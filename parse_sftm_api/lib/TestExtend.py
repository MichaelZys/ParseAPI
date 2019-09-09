# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者          :Michael.zhu
# 创建时间      :2019/9/5 14:05
# 文件          : TestExtend.py
# IDE           : PyCharm


class A(object):
    def __init__(self):
        self.a = 1
        self.b = 2



class B(A):
    def __init__(self):
        super().__init__()

c = B()
print(c.a)
