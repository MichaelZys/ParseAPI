# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者          :Michael.zhu
# 创建时间      :2019/9/4 15:41
# 文件          : properties.py
# IDE           : PyCharm


json_properties ={"employee" : \
    {
    "name": "获取员工信息",
    "api_method": "employee/v2/queryEmployee",
    "api_bodyValue": "{}",
    "schemaName": "api_sftm",
    "tableName": "['employee_v2_queryemployee_head', 'employee_v2_queryemployee_exts']"
    },

"department" : \
    {
    "name": "获取组织架构信息",
    "api_method": "organization/v1/queryOrganization",
    "api_bodyValue": "{}",
    "schemaName": "api_sftm",
    "tableName": "['organization_v1_queryorganization_head']"
    },

"dealer" : \
    {
    "name": "查询经销商",
    "api_method": "dealer/v1/queryDealer",
    "api_bodyValue": "{}",
    "schemaName": "api_sftm",
    "tableName": "['dealer_v1_querydealer_head', 'dealer_v1_querydealer_linkmans', 'dealer_v1_querydealer_deliverys',"
                 "'dealer_v1_querydealer_exts', 'dealer_v1_querydealer_stores']"
    },

"store" : \
    {
    "name": "查询门店",
    "api_method": "store/v1/queryStore",
    "api_bodyValue": "{}",
    "schemaName": "api_sftm",
    "tableName": "['store_v1_querystore_dealers', 'store_v1_querystore_deliverys', 'store_v1_querystore_exts',"
                 "'store_v1_querystore_head', 'store_v1_querystore_linkmans']"
    }}

def properties(module):
    if module in json_properties:
        return json_properties[module]
    raise(module+'不在properties文件中')

# a = properties('store')
# print(type(a))
# for x in a:
#     print(x)