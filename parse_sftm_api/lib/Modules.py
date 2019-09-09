# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者          :Michael.zhu
# 创建时间      :2019/9/3 17:18
# 文件          : Modules.py
# IDE           : PyCharm

from lib import common, pypgsql, Util
import time
import uuid
import hashlib
import urllib3
import certifi
import json


class Modules(object):
    def __init__(self, schemaName, tableName, method, openid, appkey):
        self.openid = openid
        self.appkey = appkey
        self.method = method
        self.bodyValue = '{}'
        self.schemaName = schemaName
        self.tableName = tableName

    def truncateTable(self):
        sql_truncate = 'truncate table '
        sql_list = []
        for i in self.schemaName:
            for j in self.tableName:
                sql_list.append(sql_truncate + str(i) + '.' + str(j) + ';')
        print(sql_list)
        pg = pypgsql.dba()
        pg.execListSql(sql_list)

    def getDataBaseDict(self):
        self.sqlDict, self.colDict = common.getDataBaseDict(self.schemaName, self.tableName)

    def callAPI(self):
        # 师傅通给的Demo代码
        host = 'https://openapi.waiqin365.com/api'
        timstamp = time.strftime("%Y%m%d%H%M%S")
        msgid = uuid.uuid1()
        digistSrc = '%s|%s|%s' % (self.bodyValue, self.appkey, timstamp)
        m5 = hashlib.md5()
        m5.update(digistSrc.encode('utf-8'))
        digest = m5.hexdigest()
        # print(api_bodyValue)
        url = '%s/%s/%s/%s/%s/%s' % (host, self.method, self.openid, timstamp, digest, msgid)
        print(url)
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        r = http.request('POST', url, headers={"Content-Type": "application/json", 'Accept-Encoding': 'gzip, deflate'},
                         body=self.bodyValue)

        while r.status != 200:
            print('*' * 40)
            print(r.status)
            print('*' * 40)
            r = http.request('POST', url,
                             headers={"Content-Type": "application/json", 'Accept-Encoding': 'gzip, deflate'},
                             body=self.bodyValue)

        if r.status == 200:
            data = r.data
            ret = json.loads(data.decode("utf-8"))
            # return_code = ret['return_code']
            # return_msg = ret['return_msg']
            # msg_id = ret['msg_id']
            # response_data =
            return json.loads(ret.get("response_data"))

    def dealRespnoseData(self):
        # # 全量数据先删除
        # self.truncateTable()
        # 拿到结构
        self.getDataBaseDict()
        responseData = self.callAPI()
        print('返回' + str(responseData) + '条数据')
        if len(responseData) == 0:
            return 0
        list_sql = Util.dealResponseData(responseData, self.sqlDict, self.colDict)
        print(len(list_sql))
        pg = pypgsql.dba()
        pg.execListSql(list_sql)
        return 1


class Dealer(Modules):
    def __init__(self, openid, appkey):
        schemaName = ['api_sftm']
        tableName = ['dealer_v1_querydealer_head', 'dealer_v1_querydealer_linkmans', 'dealer_v1_querydealer_deliverys',
                     'dealer_v1_querydealer_exts', 'dealer_v1_querydealer_stores']
        method = 'dealer/v1/queryDealer'
        super().__init__(schemaName, tableName, method, openid, appkey)

    def test(self):
        print(self.openid)
        print(self.appkey)
        print(self.method)
        print(self.bodyValue)
        print(self.schemaName)
        print(self.tableName)


class Store(Modules):
    def __init__(self, openid, appkey):
        schemaName = ['api_sftm']
        tableName = ['store_v1_querystore_dealers', 'store_v1_querystore_deliverys', 'store_v1_querystore_exts',
                     'store_v1_querystore_head', 'store_v1_querystore_linkmans']
        method = 'store/v1/queryStore'
        super().__init__(schemaName, tableName, method, openid, appkey)


class Department(Modules):
    def __init__(self, openid, appkey):
        schemaName = ['api_sftm']
        tableName = ['organization_v1_queryorganization_head']
        method = 'organization/v1/queryOrganization'
        super().__init__(schemaName, tableName, method, openid, appkey)


class Employee(Modules):
    def __init__(self, openid, appkey):
        schemaName = ['api_sftm']
        tableName = ['employee_v2_queryemployee_head', 'employee_v2_queryemployee_exts']
        method = 'employee/v2/queryEmployee'
        super().__init__(schemaName, tableName, method, openid, appkey)

    # def truncateTable(self):
    #     print('部门不需要删除')


class Visit(Modules):
    def __init__(self, openid, appkey):
        schemaName = ['api_sftm']
        tableName = ['cusvisit_v1_querycusvisitrecord_head']
        method = 'cusVisit/v1/queryCusVisitRecord'
        super().__init__(schemaName, tableName, method, openid, appkey)

    def truncateTable(self):
        print('路线拜访, 根据bodyValue删除')
        print(self.bodyValue)
        _body_Value = eval(self.bodyValue)
        try:
            date_start = _body_Value['date_start']
            date_end = _body_Value['date_end']
        except:
            print(' date_start :' + date_start)
            print(' date_end :' + date_end)
            raise ('date_start 和 date_end 数据异常')

        sql_truncate = 'delete from  '
        sql_list = []
        for i in self.schemaName:
            for j in self.tableName:
                sql_list.append(sql_truncate + str(i) + '.' + str(
                    j) + " where left(visit_date,10) between '" + date_start + "' and '" + date_end + "';")
        # print(sql_list)
        pg = pypgsql.dba()
        pg.execListSql(sql_list)
        # exit(2)
