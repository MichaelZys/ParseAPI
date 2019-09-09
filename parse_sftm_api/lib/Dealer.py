# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者          :Michael.zhu
# 创建时间      :2019/9/4 16:45
# 文件          : Dealer.py
# IDE           : PyCharm

from lib import Modules,common,Util


class Dealer(Modules):
    def __init__(self):
        super().__init__()
        # self._brand = brand

    def getDict(self, schemaName, tableName):
        self.schemaName = schemaName
        self.tableName = tableName
        sqlDict = {}
        colDict = {}
        for i in range(len(self.tableName)):
            _dict, _list = common.getTableListSql(self.schemaName, self.tableName[i])
            sqlDict[self.tableName[i]] = _dict
            colDict[self.tableName[i]] = _list
        return sqlDict, colDict

    # def getResponseData(self):
    #     self._brand.callAPI()
    #     pass
    #
    # def get(self, responseData, sqlDict, colDict):
    #     list_sql = Util.dealResponseData(responseData, sqlDict, colDict)
    #     pass

a = 3
dealer = Dealer()