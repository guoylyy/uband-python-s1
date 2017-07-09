#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import time;  # 引入time模块

ticks = time.time()
print "当前时间戳为:", ticks
#当前时间戳为: 1497964381.38
ticks = time.time()
localtime = time.localtime(time.time())
print '本地时间为 ：', localtime
#本地时间为 ： time.struct_time(tm_year=2017, tm_mon=6, tm_mday=20, tm_hour=21, tm_min=13, tm_sec=1, tm_wday=1, tm_yday=171, tm_isdst=0)

#最简单实用的时间格式化
localtime_2 = time.asctime( time.localtime(time.time()))
print '本地时间2为：',localtime_2
#本地时间2为： Tue Jun 20 21:13:01 2017
#其他格式化手段
print "****"
print "T1 =", time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
print "T2 =",time.strftime("%d-%m-%Y %H:%M:%S", time.localtime()) 
print "T3 =",time.strftime("%a %b %d %H:%M:%S %Y %p", time.localtime())


#%Y 四位数的年份表示（000-9999）
#%y 两位数的年份表示（00-99）
#%m 月份（01-12）
"""%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称"""
#%% %号本身


# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
#1459175064.0

##########calendar
print "calendar ————"
import calendar

cal = calendar.month(2016, 1)
print "以下输出2016年1月份的日历:"
print cal;

time1 = time.clock()
print 'time1 =', time1

t = (2009, 2, 17, 17, 3, 38, 1, 48, 0)
t = time.mktime(t)
print time.strftime("%b %d %Y %H:%M:%S", time.gmtime(t))

cal1 = calendar.calendar(2017,w=2,l=1,c=6)
print "多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。", cal1