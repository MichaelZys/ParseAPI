# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者          :Michael.zhu
# 创建时间      :2019/9/5 10:43
# 文件          : test_argv.py
# IDE           : PyCharm


import sys
import os

# print('参数个数为:', len(sys.argv), '个参数。')
# print('参数列表:', str(sys.argv))

# os.system('python3 parse_api.py --brand km --moduleAPI dealer --bodyValue {"page_number":"page_int"}')
# os.system('python3 parse_api.py --brand km --moduleAPI store --bodyValue {"page_number":"page_int"}')
# os.system('python parse_api.py --brand km --moduleAPI store --bodyValue {"page_number":"page_int"}')

# os.system('python parse_api.py --brand km --moduleAPI department --bodyValue {}')
# os.system('python parse_api.py --brand km --moduleAPI employee --bodyValue {}')
os.system('python parse_api.py --brand km --moduleAPI visit --bodyValue {\'page\':\'page_int\',\'rows\':\'1000\',\'date_start\':\'2019-09-05\',\'date_end\':\'2019-09-07\'}')





# 经销商
# python3 parse_api.py --brand km --moduleAPI dealer --bodyValue {"page_number":"page_int"}

# 门店
# python3 parse_api.py --brand km --moduleAPI store --bodyValue {"page_number":"page_int"}
# python3 /usr/project/python/parse_sftm_api_v4/parse_api.py --brand km --moduleAPI store --bodyValue {"page_number":"page_int"}

# 组织架构
# python3 parse_api.py --brand km --moduleAPI department --bodyValue {}
# python3 /usr/project/python/parse_sftm_api_v4/parse_api.py --brand km --moduleAPI department --bodyValue {}

# 员工
# python3 parse_api.py --brand km --moduleAPI employee --bodyValue {}
# python3 /usr/project/python/parse_sftm_api_v4/parse_api.py --brand km --moduleAPI employee --bodyValue {}

# 实际拜访
# python3 parse_api.py --brand km --moduleAPI visit --bodyValue "{'page':'page_int','rows':'1000','date_start':'$(date +%Y-%m-%d --date="-1 day")','date_end':'$(date +%Y-%m-%d --date="-1 day")'}"
# python3 /usr/project/python/parse_sftm_api_v4/parse_api.py --brand km --moduleAPI visit --bodyValue "{'page':'page_int','rows':'1000','date_start':'$(date +%Y-%m-%d --date="-1 day")','date_end':'$(date +%Y-%m-%d --date="-1 day")'}"