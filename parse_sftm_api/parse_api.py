# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者          :Michael.zhu
# 创建时间      :2019/9/5 10:35
# 文件          : parse_api.py
# IDE           : PyCharm

import sys
import getopt
from lib import common


# 输入参数1 brand = ['km','ky','by']

# 输入参数2 api = ['dealer','store','department','employee']
# 输入参数3 api_bodyValue = '{}'   默认, 回单和路线， 可能涉及到时间

def parser_argv(argv):
    brand = ''
    moduleAPI = ''
    bodyValue = '{}'
    try:
        opts, args = getopt.getopt(argv, "b:m:v", ["brand=", "moduleAPI=", "bodyValue="])
    except getopt.GetoptError:
        print('请按照以下格式输入')
        print('parse_api.py --brand <exapmle:km> --moduleAPI <exapmle:dealer> --bodyValue <exapmle:{}>')
        sys.exit(2)

    for opt, arg in opts:
        if opt == '-h':
            print('test.py -i <inputfile> -o <outputfile>')
            sys.exit()
        elif opt in ("-b", "--brand"):
            brand = arg
        elif opt in ("-m", "--moduleAPI"):
            moduleAPI = arg
        elif opt in ("-v", "--bodyValue"):
            bodyValue = arg

    return brand, moduleAPI, bodyValue


if __name__ == '__main__':
    print(sys.argv)
    # 解析command line
    brand, moduleAPI, bodyValue = parser_argv(sys.argv[1:])

    # new brand()
    brand = common.getBrand(brand)

    # new Module()
    module = common.getModule(brand, moduleAPI)

    # 全量初始化
    # 不需要的模块， 可以重写这个方法
    module.bodyValue = bodyValue
    module.truncateTable()
    # exit(2)
    # Save ResponseData
    # print(eval(bodyValue)['page'])
    if 'page' in bodyValue:
        page_int = 0
        # print(page_int)
        while True:
            page_int += 1
            module.bodyValue = bodyValue.replace('page_int',str(page_int))
            print(module.bodyValue)
            # exit(2)
            if module.dealRespnoseData() == 0:
                break

    else:
        # print('else')
        module.dealRespnoseData()



