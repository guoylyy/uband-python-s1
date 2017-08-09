#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: youngmpjlt
#日期和时间 time calender

#获取时间戳
import time; #引入time模块

ticks = time.time()
print '当前时间戳为:', ticks

localtime = time.localtime(time.time())
print '本地时间为:',localtime #获取当前时间

localtime = time.asctime(time.localtime(time.time()))
print '本地时间为 :',localtime #获取格式化的时间 #Thu Apr 7 10:05:21 2016

#格式化日期

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime()) #2016-04-07 10:25:09
print time.strftime('%a %b %d %H:%M:%S',time.localtime()) #Thur Apr 07 10:25:09 2016

a = 'Sat Mar 28 22:24:24 2016'
print time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y')) #出来时间戳：1459175064.0

import calendar

cal = calendar.month(2017,8)
print '以下输出2017年8月份的日历'
print cal;

import datetime
i = datetime.datetime.now()
print ('当前的日期和时间是 %s' % i)
print ('ISO格式的日期和时间是 %s' % i.isoformat())
print ('当前的年份是 %s' %i.year)
print ('当前的月份是 %s' %i.month)
print ('当前的日期是 %s' %i.day)
print ('dd/mm/yyyy 格式是 %s/%s/%s' %(i.day, i.month, i.year))
print ('当前小时是 %s' %i.hour)
print ('当前分钟是 %s' %i.minute)
print ('当前秒是 %s' %i.second)




