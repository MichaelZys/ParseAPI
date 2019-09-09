# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者        :Michael.zhu
# 创建时间      :2019/9/3 10:25
# 文件          : Department.py
# IDE           : PyCharm

from lib.ObjectAPI import KangMian
from lib.ParseModules import ParseEmployee
from lib import Util
from lib import pypgsql


def department():
    api_method = 'organization/v1/queryOrganization'
    # api_bodyValue= ''
    km = KangMian(api_method, '{}')
    responseData = km.callAPI()
    # print(type(responseData))
    print(responseData)


def employee():
    api_method = 'employee/v2/queryEmployee'
    # api_bodyValue= ''
    km = KangMian(api_method, '{}')
    responseData = km.callAPI()
    emp = ParseEmployee()
    sqlDict, colDict = emp.getTabAndSql_Dict()

    list_sql = Util.dealResponseData(responseData, sqlDict, colDict)
    print(len(list_sql))
    pg = pypgsql.dba()
    pg.execListSql(list_sql)


if __name__ == '__main__':
    # global list_sql
    employee()
    department()
