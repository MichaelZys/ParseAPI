# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者          :Michael.zhu
# 创建时间      :2019/9/5 12:30
# 文件          : Brand.py
# IDE           : PyCharm


class Brand(object):
    def __init__(self, openid, appkey):
        self.openid = openid
        self.appkey = appkey
    pass

class KangMian(Brand):
    def __init__(self):
        super().__init__('', '')
    pass

class KangYin(Brand):
    pass

class BaiYin(Brand):
    pass

#
# km = KangMian()
#
# print(km.openid)
# print(km.appkey)