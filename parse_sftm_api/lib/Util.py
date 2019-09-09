# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者          :Michael.zhu
# 创建时间      :2019/9/3 15:09
# 文件          : util.py
# IDE           : PyCharm

import sys

# 处理List level的数据，
# 这个List都是子表的数据， head和子表是一对多的关系。
# 然后再调用dealRow
# 返回数组Sql
def dealListRow(perData, sqlInsert, collist, tableName):
    list_sql = []
    _tableName = tableName[tableName.rindex('_')+1:]
    if _tableName in perData:
        for i in range(len(perData[_tableName])):
            list_sql.append(dealRow(perData[_tableName][i], sqlInsert, collist))
    return list_sql

    # sys.exit(0)



# 处理行level的数据，
# 这个行，可能是head(因为head只有一条数据)， 也可能是其他子表拆分出来的一行
# 返回一条Sql
def dealRow(perData, sqlInsert, collist):
    sql_values = ''
    for index_col in range(len(collist)):
        if collist[index_col] not in perData:
            perData[collist[index_col]] = ''
        try:
            values = str(perData[collist[index_col]]).replace("'", '')
        except:
            # print(perData)
            # print(collist[index_col])
            # print(perData[collist[index_col]])
            raise ('2')
        sql_values = sql_values + "'" + str(values) + "',"
    _sql = sqlInsert + sql_values[:-1] + ');'
    # print(_sql)
    return _sql

#处理API返回的数据
#根据模块对应的表
#返回List数组sql
def dealResponseData(responseData, sqlDict, colDict):
    list_sql = []
    for perData in range(len(responseData)):
        # print(type(responseData[perData]))
        # print(responseData[perData])
        for wc in colDict:
            # print(wc)
            if 'head' in wc:
                list_sql.append(dealRow(responseData[perData], sqlDict[wc], colDict[wc]))
            else:
                list_sql.extend(dealListRow(responseData[perData], sqlDict[wc], colDict[wc], wc))
    return list_sql



# if __name__ == '__main__':
    # print(type(responseData))
    # print(len(responseData))
    # dealResDataAndTablist(responseData, sqlDict, colDict)