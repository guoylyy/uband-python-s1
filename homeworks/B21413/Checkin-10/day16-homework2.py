#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 190

import time

def main():
	print 'time.time(): %f' % time.time() #返回当前时间的时间戳
	print time.localtime(time.time()) #本地时间的函数
	print time.asctime(time.localtime(time.time())) #里面的括号要有层次哈 
													#获取格式化的时间

if __name__ == '__main__':
  main()