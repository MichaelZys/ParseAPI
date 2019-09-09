# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者        :Michael.zhu
# 创建时间      :2019/9/3 10:10
# 文件          : ObjectAPI.py
# IDE           : PyCharm

import time
import uuid
import hashlib
import urllib3
import certifi
import json


class ObjectAPI(object):
    # def __init__(self, api_openid, api_appkey, api_method, api_bodyValue):
    #     self.openid = api_openid
    #     self.appkey = api_appkey
    #     self.method = api_method
    #     self.bodyValue = api_bodyValue

    def callAPI(self, api_openid, api_appkey, api_method, api_bodyValue):

        # 师傅通给的Demo代码
        host = 'https://openapi.waiqin365.com/api'
        timstamp = time.strftime("%Y%m%d%H%M%S")
        msgid = uuid.uuid1()
        digistSrc = '%s|%s|%s' % (api_bodyValue, api_appkey, timstamp)
        m5 = hashlib.md5()
        m5.update(digistSrc.encode('utf-8'))
        digest = m5.hexdigest()
        # print(api_bodyValue)
        url = '%s/%s/%s/%s/%s/%s' % (host, api_method, api_openid, timstamp, digest, msgid)
        print(url)
        http = urllib3.PoolManager(cert_reqs='CERT_REQUIRED', ca_certs=certifi.where())
        r = http.request('POST', url, headers={"Content-Type": "application/json", 'Accept-Encoding': 'gzip, deflate'},
                         body=api_bodyValue)

        while r.status != 200:
            print('*' * 40)
            print(r.status)
            print('*' * 40)
            r = http.request('POST', url,
                             headers={"Content-Type": "application/json", 'Accept-Encoding': 'gzip, deflate'},
                             body=api_bodyValue)

        if r.status == 200:
            data = r.data
            ret = json.loads(data.decode("utf-8"))
            # return_code = ret['return_code']
            # return_msg = ret['return_msg']
            # msg_id = ret['msg_id']
            response_data = json.loads(ret.get("response_data"))
            return response_data


class KangMian(ObjectAPI):
    def __init__(self, api_method, api_bodyValue):
        self.openid = ''
        self.appkey = ''
        self.method = api_method
        self.bodyValue = api_bodyValue

    def callAPI(self):
        return super().callAPI(self.openid, self.appkey, self.method, self.bodyValue)

    pass

class KangYin(ObjectAPI):
    def __init__(self, api_openid, api_appkey, api_method, api_bodyValue):
        self.openid = api_openid
        self.appkey = api_appkey
        self.method = api_method
        self.bodyValue = api_bodyValue
    pass

class BaiYin(ObjectAPI):
    def __init__(self, api_openid, api_appkey, api_method, api_bodyValue):
        self.openid = api_openid
        self.appkey = api_appkey
        self.method = api_method
        self.bodyValue = api_bodyValue
    pass