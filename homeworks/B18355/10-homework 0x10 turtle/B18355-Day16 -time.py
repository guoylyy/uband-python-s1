#!/usr/bin/python
#-*- coding:utf-8 -*-
# Filename test_010.py
# 题目：暂停一秒输出，并格式化当前时间。
# 分析：time模块Go on
import time

def delay(n):
	time.sleep(n)


def format_time():
	print time.time()
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())

	delay(1)
	print time.time()
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

if __name__ == '__main__':
	format_time()