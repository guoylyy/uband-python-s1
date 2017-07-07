#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: chendasuan

import time
ticks = time.time()
print '当时时间截为： ',ticks#时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。
print'-------'
localtime = time.localtime(time.time())
print '本地时间: ',localtime
print '------'
localtime = time.asctime( time.localtime(time.time()) )
print '本地时间为:', localtime

print '----'
print time.strftime("%Y-%m-%d %H:%M:%S %Y", time.localtime())
print '-----'
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print '-----'
a = "Sat Jun 24 10:43:32 2017" 
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

print'---calendar---'
import calendar

cal = calendar.month(2017, 1)
print "以下输入2017年1月份的日历："
print cal;
ca = calendar.monthcalendar(2017,6)
print ca;