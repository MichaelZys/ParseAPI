# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者        :Michael.zhu
# 创建时间      :2019/9/3 14:28
# 文件          : common.py
# IDE           : PyCharm

from lib import pypgsql, Brand, Modules
from lib import ObjectAPI
from lib import Modules
import properties

# 通过 schemaName 和 tableName
# 获得数据库信息
# 表的insert部分 例如 insert schema.table(col1, col2...) values( 用于拼接sql语句
# 表的col部分 例如 [col1,col2..] 用于导入数据
# 返回sqlDict 不同表的Insert Part sql语句
# 返回colDict 不同表的列List
def getDataBaseDict(schemaName, tableName):
    if len(schemaName) == 0 or len(tableName) == 0:
        raise ('schemaName 和 tableName 不能为空')
    # self.schemaName = schemaName
    # self.tableName = tableName
    sqlDict = {}
    colDict = {}
    for j in range(len(schemaName)):
        for i in range(len(tableName)):
            _dict, _list = getTableListSql(schemaName[j], tableName[i])
            sqlDict[tableName[i]] = _dict
            colDict[tableName[i]] = _list
    return sqlDict, colDict

# 通过参数， 调用模块
def getModule(brand, module):
    if module == 'dealer':
        from lib.Modules import Dealer
        return Dealer(brand.openid, brand.appkey)
    elif module == 'store':
        from lib.Modules import Store
        return Store(brand.openid, brand.appkey)
    elif module == 'department':
        from lib.Modules import Department
        return Department(brand.openid, brand.appkey)
    elif module == 'employee':
        from lib.Modules import Employee
        return Employee(brand.openid, brand.appkey)
    elif module == 'visit':
        from lib.Modules import Visit
        return Visit(brand.openid, brand.appkey)
    else:
        raise ('没有此模块')


# # 解析拿到的response
# def parseResponseData(responseData):
#     sqlDict, colDict = Employee().getDict(schemaName, tableName)
#
#     retrun Util.dealResponseData(responseData, sqlDict, colDict)

# 拿到模块对应的数据库信息
# def getDataBaseInfo(brand, api_method, api_bodyValue):
#     if brand == 'dealer':
#         return Modules.Employee()
#     elif brand == 'ky':
#         pass
#     elif brand == 'by':
#         pass

def getDict(schemaName, tableName):
    sqlDict = {}
    colDict = {}
    for i in range(len(tableName)):
        _dict, _list = getTableListSql(schemaName, tableName[i])
        sqlDict[tableName[i]] = _dict
        colDict[tableName[i]] = _list
    return sqlDict, colDict


# 拿到品牌对应的属性
# 返回该品牌的类
def getBrand(brand, api_method, api_bodyValue):
    if brand == 'km':
        return ObjectAPI.KangMian(api_method, api_bodyValue)
    elif brand == 'ky':
        pass
    elif brand == 'by':
        pass
    else:
        raise ('没有此品牌：' + brand)


# 20190905 要替代上面的方法
def getBrand(brand):
    if brand == 'km':
        return Brand.KangMian()
    elif brand == 'ky':
        pass
    elif brand == 'by':
        pass
    else:
        raise ('没有此品牌：' + brand)


# 拿到某块对应的属性
def getModuleProperties(module):
    dict_moduleInfo = properties.properties(module)
    return dict_moduleInfo


def getTableList(schemaName, tableName):
    sql = '''
        select attr.attname
        from pg_attribute as attr
        left join pg_class  as cls on attr.attrelid = cls.oid 
        inner join pg_description as des on attr.attrelid = des.objoid and attr.attnum = des.objsubid
        inner join pg_namespace as ns on cls.relnamespace = ns.oid
        where ns.nspname='%s' and cls.relname='%s' 
        and des.description ~ 'WQ';
    ''' % (schemaName, tableName)
    pg = pypgsql.dba()
    result = pg.execSqlFetchall(sql)
    list_columns = []
    # print(type(result))
    for i in result:
        # print(type(i))
        list_columns.append(i['attname'])
        # print(i['attname'])
    return list_columns


def getTableListSql(schemaName, tableName):
    list_columns = getTableList(schemaName, tableName)

    sql_insert = " insert into %s.%s(   " % (schemaName, tableName)
    for x in range(len(list_columns)):
        sql_insert = sql_insert + list_columns[x] + ','
    sql_insert = sql_insert[:-1] + ') values ('
    return sql_insert, list_columns

# getTableList('api_sftm', 'employee_v2_queryemployee_head')
