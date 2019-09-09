# !/usr/bin/python3
# -*- coding: utf-8 -*-
# 作者          :Michael.zhu
# 创建时间      :2019/9/5 10:54
# 文件          : test_getopt.py
# IDE           : PyCharm

import sys, getopt

def main(argv):
    print(argv)
    inputfile = ''
    outputfile = ''
    try:
      opts, args = getopt.getopt(argv,"i:o:",["ifile=","ofile="])
    except getopt.GetoptError:
      print('test.py -i <inputfile> -o <outputfile>')
      sys.exit(2)
    for opt, arg in opts:
      if opt == '-h':
         print('test.py -i <inputfile> -o <outputfile>')
         sys.exit()
      elif opt in ("-i", "--ifile"):
         inputfile = arg
      elif opt in ("-o", "--ofile"):
         outputfile = arg
    print('输入的文件为：', inputfile)
    print('输出的文件为：', outputfile)

if __name__ == "__main__":
    print(sys.argv)
    main(sys.argv[1:])