# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者          :Michael.zhu
# 创建时间      :2019/9/4 12:15
# 文件          : Customer.py
# IDE           : PyCharm

import sys
import os
par_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(par_dir)
from lib import Util, pypgsql, common
from lib.ObjectAPI import KangMian
from lib.Modules import Employee
import time

# 查询门店
api_method = 'store/v1/queryStore'
api_bodyValue = '{}'
schemaName = ['api_sftm']
tableName = ['store_v1_querystore_dealers', 'store_v1_querystore_deliverys', 'store_v1_querystore_exts',
             'store_v1_querystore_head', 'store_v1_querystore_linkmans']

pg = pypgsql.dba()
sql_truncate = 'truncate table '
for _ in tableName:
    _sql = sql_truncate + schemaName + '.' + _ + ';'
    print(_sql)
    pg.execsql(_sql)

i = 0
while True:
    i += 1
    api_bodyValue = '{"page_number":"'+str(i)+'"}'
    print(api_bodyValue)
    # exit(0)
    km = KangMian(api_method, api_bodyValue)
    # 拿到ResponData
    responseData = km.callAPI()
    if len(responseData) == 0:
        break
    # 拿到对应的数据库结构
    sqlDict, colDict = common.getDict(schemaName, tableName)

    list_sql = Util.dealResponseData(responseData, sqlDict, colDict)
    print(len(list_sql))
    t1 = time.time()

    pg.execListSql(list_sql)
    print(time.time() - t1)
