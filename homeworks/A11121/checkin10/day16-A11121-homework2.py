#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Jinxiao 

#time 库的引用
import time
#时间戳
ticks = time.time()
print '当前时间戳：',ticks
#时间间隔是以秒为单位的浮点小数。每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
#localtime()获取当前时间
localtime = time.localtime(time.time())
print '本地时间为：',localtime
#asctime() 获取可读时间模式的函数
localtime = time.asctime(time.localtime(time.time()))
print '本地时间为：',localtime
#time模块的strftime来格式化日期 time.strftime(format[,t])
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

print time.strftime('%a %b %d %H:%M:%S %Y',time.localtime())
a = 'Tue Jun 20 13:00:10 2017'
print time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y'))

'''
python中时间日期格式化符号：
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
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
%Z 当前时区的名称
%% %号本身
'''

pans = time.timezone
print '当前时区距离格林威治时间为',pans