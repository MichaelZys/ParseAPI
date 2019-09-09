# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者          :Michael.zhu
# 创建时间      :2019/9/4 15:10
# 文件          : test_path.py
# IDE           : PyCharm
#
# import os
# par_dir = os.path.dirname(os.path.abspath(__file__))
# print(par_dir)
# # os.chdir(par_dir)
#
# from lib import *
# # common.getTableList('','')
# print(dir())

from datetime import datetime as dt
import datetime

datetime.timedelta(days=1)
date_frm = date_end = (dt.now() - datetime.timedelta(days=1)).strftime('%Y-%m-%d')

print(date_frm,date_end)

