#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: vera

def time():
	import time
	ticks = time.time()
	print '当前时间为：', ticks

	localtime = time.localtime(time.time())
	print '本地时间为', localtime

	localtime = time.asctime(time.localtime(time.time()))
	print '本地时间为', localtime

	clock = time.clock()
	print '当前时间为：', clock

def calendar():
	import calendar
	cal = calendar.month(2017, 6)
	print 'calendar of June, 2017:'
	print cal

if __name__ == '__main__':
	time()
	calendar()