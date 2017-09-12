#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: suancaiyu
#学习内容 库的引用 怎么导入一个库, 库是什么? 怎么构建一个库 库的方法怎么调用 ，怎么查询库有哪些方法可以调用
#预习 python  时间库  参考 python  菜鸟教程
import time;    #后面注意加分号


now = time.time()     #时间戳
print 'now is:', now


localtime = time.localtime(time.time())
print 'the local time is:', localtime

# 最简单的可读时间模式函数是asctime()
localtime = time.asctime(time.localtime(time.time()))   
print '本地时间为:', localtime

print '--------'
# time.strftime(format[,t])
#格式化成xxxx-xx-xx  xx:xx:xx形式
print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  
#犯的错误：timestrftime 忘记加中间的点  第二点注意其中的大小写，H S都是必须大写的

#格式化成 Sat Mar 28 xx:xx:xx xxxx
print time.strftime('%a %b %d %H:%M:%S %Y',time.localtime())
# %a是英文星期 %b是英文月份 %d是日期

#将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a, '%a %b %d %H:%M:%S %Y'))

#     %y 两位数的年份表示（00-99）
#     %Y 四位数的年份表示（000-9999）
#     %m 月份（01-12）
#     %d 月内中的一天（0-31）
#     %H 24小时制小时数（0-23）
#     %I 12小时制小时数（01-12）
#     %M 分钟数（00=59）
#     %S 秒（00-59）
#     %a 本地简化星期名称
#     %A 本地完整星期名称
#     %b 本地简化的月份名称
#     %B 本地完整的月份名称
#     %c 本地相应的日期表示和时间表示
#     %j 年内的一天（001-366）
#     %p 本地A.M.或P.M.的等价符
#     %U 一年中的星期数（00-53）星期天为星期的开始
#     %w 星期（0-6），星期天为星期的开始
#     %W 一年中的星期数（00-53）星期一为星期的开始
#     %x 本地相应的日期表示
#     %X 本地相应的时间表示
#     %Z 当前时区的名称
#     %% %号本身



print '------calendar'

#尝试1  把月份加上变量
import calendar
year = 2017     
month = 6

cal = calendar.month(year,month)
print '以下输出%d年%d月份的日历：' % (year, month)
print cal;

print '---------'

import calendar

calendar = calendar.calendar(year, w=2, l=1, c=6)
print '以下是2017年的日历：'    #这边不加冒号出不来
print calendar;        #注意结尾的分号  一定要加的

import calendar
x = calendar.monthrange(year,month)
print x;
