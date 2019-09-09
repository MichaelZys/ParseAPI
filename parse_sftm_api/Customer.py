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

main_brand = ['km']
main_modules = ['dealer']
# main_modules = ['dealer', 'store']

for brand in main_brand:
    for module in main_modules:
        print(module)
        # 拿到模块的配置属性
        dict_moduleInfo = common.getModuleProperties(module)

        # 拿到品牌的配置属性
        brandObjec = common.getBrand(brand,dict_moduleInfo['api_method'], dict_moduleInfo['api_bodyValue'])

        # 调用api
        responseData = brandObjec.callAPI()

        # 拿到模块对应的数据库信息
        sqlDict, colDict = common.getDict(dict_moduleInfo['api_method'], dict_moduleInfo['api_bodyValue'])

        # 解析拿到的response
        list_sql = Util.dealResponseData(responseData, sqlDict, colDict)

        # 存储到pgsql
        print(len(list_sql))
        t1 = time.time()
        pg = pypgsql.dba()
        pg.execListSql(list_sql)
        print(time.time() - t1)

exit(0)
















# 查询经销商
api_method = 'dealer/v1/queryDealer'
api_bodyValue = '{}'
schemaName = 'api_sftm'
tableName = ['dealer_v1_querydealer_head', 'dealer_v1_querydealer_linkmans', 'dealer_v1_querydealer_deliverys',
             'dealer_v1_querydealer_exts', 'dealer_v1_querydealer_stores']
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
    sqlDict, colDict = Employee().getDict(schemaName, tableName)

    list_sql = Util.dealResponseData(responseData, sqlDict, colDict)
    print(len(list_sql))
    t1 = time.time()
    pg = pypgsql.dba()
    pg.execListSql(list_sql)
    print(time.time() - t1)


# 查询门店
api_method = 'store/v1/queryStore'
api_bodyValue = '{}'
schemaName = 'api_sftm'
tableName = ['store_v1_querystore_dealers', 'store_v1_querystore_deliverys', 'store_v1_querystore_exts',
             'store_v1_querystore_head', 'store_v1_querystore_linkmans']
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
    sqlDict, colDict = Employee().getDict(schemaName, tableName)

    list_sql = Util.dealResponseData(responseData, sqlDict, colDict)
    print(len(list_sql))
    t1 = time.time()
    pg = pypgsql.dba()
    pg.execListSql(list_sql)
    print(time.time() - t1)
