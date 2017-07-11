#!/usr/bin/python
#_*_ coding:utf-8 _*_
#@author:B20840

import time;
import calendar

ticks = time.time()
print "Current time is:", ticks

#localtime=time.localtime(time.time())
localtime=time.asctime(time.localtime(time.time()))
print"Local time is:", localtime

#格式化
print time.strftime("%Y-%m-%d %H:%M:%S %Y",time.localtime())
a="Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

cal= calendar.month(2016,1)
print "以下输出2016年1月的日历："
print cal;