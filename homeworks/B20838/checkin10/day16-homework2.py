#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:lightningLUO

import time;
#函数time.time()用于获取当前时间戳,每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示
#时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年
ticks = time.time()
print '当前时间戳为:',ticks
#获取当前时间
localtime = time.localtime(time.time())
print '本地时间为：', localtime
#获取格式化的时间
localtime = time.asctime(time.localtime(time.time()))
print '本地时间为：', localtime
#格式化日期
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print time.strftime('%A %B %d %H:%M:%S %Y',time.localtime())
a = 'Sun Jun 25 17:24:29 2017'
print time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y'))


import calendar

cal = calendar.month(2017,6)
print '2017年6月份的日历：'
print cal

