#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY

#时间间隔是以秒为单位的浮点小数
#每个时间戳都以自从1970年1月1日午夜（历元）经过了多长时间来表示。
import time; # 引入time模块

ticks = time.time() #函数time.time()用于获取当前时间戳
print ' 当前时间戳为：',ticks 
#时间戳单位最适于做日期运算。但是1970年之前的日期就无法以此表示了。太遥远的日期也不行，UNIX和Windows只支持到2038年。

#localtime = time.locktime()
#获取当前时间
localtime1 = time.localtime(ticks) #从返回浮点数的时间辍方式向时间元组转换，只要将浮点数传递给如localtime之类的函数。
print ' 本地时间为： ', localtime1
#tm_isdst夏令时	-1, 0, 1, -1是决定是否为夏令时的旗帜

#获取格式化的时间
localtime2 = time.asctime(localtime1) 
#最简单的获取可读的时间模式的函数是asctime() 
#time.asctime([tupletime]) 接受时间元组并返回一个可读的形式为"Tue Dec 11 18:07:14 2008"（2008年12月11日 周二18时07分14秒）的24个字符的字符串。
print ' 本地时间为：', localtime2

#格式化日期
#格式化成2016-03-20 11:45:39形式
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()) #strftime 接收以时间元组，并返回以可读字符串表示的当地时间，格式由fmt决定。
# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
# 格式化成Sat Mar 28 22:24:24 2016形式
a = 'Wed Jun 21 09:27:30 2017'
print time.mktime(time.strptime(a, '%a %b %d %H:%M:%S %Y')) #mktime 接受时间元组并返回时间辍（1970纪元后经过的浮点秒数）strptime根据fmt的格式把一个时间字符串解析为时间元组。

# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身

#获取某月日历
import calendar

cal = calendar.month(2017,6,w = 3, l =1) #逗号谨记  #calendar.month(year,month,w=2,l=1) 返回一个多行字符串格式的year年month月日历，两行标题，一周一行。每日宽度间隔为w字符。每行的长度为7* w+6。l是每星期的行数。
print '以下输出2017年6月份的日历：'
print cal

calendar.setfirstweekday(1) #设置每周的起始日期码。0（星期一）到6（星期日）
cal = calendar.calendar(2017, w = 2, l = 1, c = 6) #calendar.calendar(year,w=2,l=1,c=6)返回一个多行字符串格式的year年年历，3个月一行，间隔距离为c。 每日宽度间隔为w字符。每行长度为21* W+18+2* C。l是每星期行数。
print '以下输出2017年的日历'
print cal