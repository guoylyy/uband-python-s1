#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Xiangwan


import time
t = time.time()
print '当前时间戳为: ', t
localtime = time.localtime(time.time())#获取当地时间下的时间元组，tm_isdst=0因为是夏令时，否则为1
print '本地时间为: ', localtime#定义的localtime可以改

localtime2 = time.asctime(time.localtime(time.time()))#用时间元组获取格式化的时间
print '本地时间为: ', localtime2

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())#格式化日期
print time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())#同上，接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
a = 'Tue Jul 25 16:27:24 2017'
print time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y'))#time.strptime(str,fmt='%a %b %d %H:%M:%S %Y')是根据fmt的格式把时间字符再解析为时间元组
                                                          #time.mktime()是接受时间元组并返回时间戳，所以这里写localtime(time.time())也可以
print 'time altzone %d ' % time.altzone#函数返回格林威治西部的夏令时地区的偏移秒数,China在格林威治的东部，所以为负(也包括英国，西欧)

localtime3 = time.gmtime(time.time())#tm_isdst始终为0
print '格林威治时间为：', localtime3

t0 = time.clock()#计算系统进程运行的真实时间，很精确..电脑好慢啊！
print time.clock()

def procedure():
	time.sleep(5)#推迟程序运行的时间——这里是5秒
t1 = time.time()
procedure()
print time.time() - t1

import calendar#获取某月日历
cal = calendar.month(2017,7)
print '以下输出2017年7月份的日历：'
print cal
print calendar.isleap(2017)#检查是否是闰年
print calendar.leapdays(1991,2017)#计算1991-2917年之间的闰年总数
