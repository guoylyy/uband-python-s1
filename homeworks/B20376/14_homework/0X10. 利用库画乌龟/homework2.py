#! usr/bin/python
# -*- coding: utf-8 -*-
# @author:Emma

import time

def homework1():
	ticks = time.time()
	print '当前时间为:',ticks

	#获取当前时间
	localtime = time.localtime(time.time())
	print '本地时间为:',localtime

	#获取格式化的时间
	localtime = time.asctime(time.localtime(time.time()))
	print '本地时间为:',localtime

	#格式化日期
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
	print time.strftime('%a %b %d %H:%M:%S %Y',time.localtime())

	#将格式字符串转换为时间戳
	a = 'Sat Mar 28 22:24:24 2016'
	print time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y'))


import calendar

def homework2():
	#获取某月日历
	cal = calendar.month(2017,6)
	print '以下输出2017年6月份的日历:'
	print cal;

if __name__ == '__main__':
	homework1()
	homework2()