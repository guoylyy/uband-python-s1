#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Winnie

import time;
ticks = time.time()
print '当前时间为：', ticks

localtime = time.localtime(time.time())
print '本地时间为:', localtime

localtime = time.asctime(time.localtime(time.time()))
print  '本地时间为：',localtime

#格式化成2017-06-20 
print time.strftime("%Y-%m-%d %H:%m:%S", time.localtime())
#格式化成 Tue Jun 20 
print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())
# 将格式字符串转换为时间戳
a = "Tue Jun 20 11:10:13 2017"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

import calendar
cal = calendar.month(2017,6)
print '以下输出2017年6月的日历：'
print cal

