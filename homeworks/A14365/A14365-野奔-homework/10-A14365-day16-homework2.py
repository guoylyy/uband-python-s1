#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
#时间戳
ticks = time.time()
print "当前时间戳为： ", ticks
#获取当前时间
localtime = time.localtime(time.time())
print "本地时间为:", localtime
#获取格式化时间
localtime = time.asctime( localtime ) # 等于localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为：", localtime
#格式化日期
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, "%a %b %d %H:%M:%S %Y"))


import calendar

cal = calendar.month(2016,1)
print "以下输出2016年1月份的日历："
print cal

