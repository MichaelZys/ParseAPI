# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者        :Michael.zhu
# 创建时间      :2019/9/3 11:03
# 文件          : ParseListInfo.py
# IDE           : PyCharm

from lib import common


class ParseModules(object):
    def __init__(self, a, *args):
        pass

    def parseSingleList(self):
        pass

    def parseMultyList(self):
        pass


class ParseDepartment(ParseModules):
    def __init__(self):
        pass

    # 获取相关表的插入数组
    def aaa(self):
        pass


class ParseEmployee(ParseModules):
    def __init__(self):
        self.schemaName = 'api_sftm'
        self.tableName = ['employee_v2_queryemployee_head', 'employee_v2_queryemployee_exts']

    def getTabAndSql_Dict(self):
        sqlDict = {}
        colDict = {}
        for i in range(len(self.tableName)):
            _dict, _list = common.getTableListSql(self.schemaName, self.tableName[i])
            sqlDict[self.tableName[i]] = _dict
            colDict[self.tableName[i]] = _list
        return sqlDict, colDict


# if __name__ == '__main__':
#     b = ParseEmployee()
#     b.getTabAndSql_Dict()
