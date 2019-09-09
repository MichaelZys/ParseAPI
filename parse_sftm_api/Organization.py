# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者          :Michael.zhu
# 创建时间      :2019/9/4 11:43
# 文件          : Organization.py
# IDE           : PyCharm

# 这个类主要获取两部分数据。
# 1. 员工数据。
# 2. 组织架构数据。

import sys
import os
par_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(par_dir)
from lib import Util, pypgsql
from lib.ObjectAPI import KangMian
from lib.Modules import Employee
import time

# 获取员工信息
api_method = 'employee/v2/queryEmployee'
api_bodyValue = '{}'
schemaName = 'api_sftm'
tableName = ['employee_v2_queryemployee_head', 'employee_v2_queryemployee_exts']

km = KangMian(api_method, api_bodyValue)
# 拿到ResponData
responseData = km.callAPI()
# 拿到对应的数据库结构
sqlDict, colDict = Employee().getDict(schemaName,tableName)

list_sql = Util.dealResponseData(responseData, sqlDict, colDict)
print(len(list_sql))
t1 = time.time()
pg = pypgsql.dba()
pg.execListSql(list_sql)
print(time.time()-t1)




# 获取组织架构信息
api_method = 'organization/v1/queryOrganization'
api_bodyValue = '{}'
schemaName = 'api_sftm'
tableName = ['organization_v1_queryorganization_head']

km = KangMian(api_method, api_bodyValue)
# 拿到ResponData
responseData = km.callAPI()
# 拿到对应的数据库结构
sqlDict, colDict = Employee().getDict(schemaName,tableName)

list_sql = Util.dealResponseData(responseData, sqlDict, colDict)
print(len(list_sql))
t1 = time.time()
pg = pypgsql.dba()
pg.execListSql(list_sql)
print(time.time()-t1)
