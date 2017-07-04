#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time

ticks = time.time()
print '当前时间戳为:', ticks

localtime = time.localtime(time.time())
print '本地时间为:', localtime

localtime = time.asctime(time.localtime(time.time()))
print '本地时间为:', localtime

import time
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

print time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())

a = 'Tue Jun 20 09:02:56 2017'
print time.mktime(time.strptime(a, '%a %b %d %H:%M:%S %Y'))

import calendar

cal = calendar.month(2017, 6)
print '以下输出2017年6月份的日历:'
print cal;