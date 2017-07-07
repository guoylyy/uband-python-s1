#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import calendar
import datetime

ticks = time.time()
print "当前时间戳为： ",ticks

localtime = time.localtime(ticks)
print "本地时间为：", localtime

flocaltime = time.asctime(localtime)
print "格式化的本地时间为：", flocaltime

# 格式化成YYYY-MM-DD HH:MM:SS形式
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

# 格式化成Sat Mar 28 HH:MM:SS YYYY形式
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 
  
# 将格式字符串转换为时间戳
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

# python中时间日期格式化符号：
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
print "------calendar------"

cal = calendar.month(2016, 1)
print "以下输出2016年1月的日历：\n"
print cal

# Python time altzone() 函数返回格林威治西部的夏令时地区的偏移秒数。
# 如果该地区在格林威治东部会返回负值（如西欧，包括英国）。
# 对夏令时启用地区才能使用。
print "time.altzone: %d" % time.altzone

# 作用相当于asctime(localtime(secs))，未给参数相当于asctime()
print time.ctime(ticks)
print time.ctime()

# Python time sleep() 函数推迟调用线程的运行，
# 可通过参数secs指秒数，表示进程挂起的时间。
print "Start : %s" % time.ctime()
time.sleep( 3 )
print "End : %s" % time.ctime()

# 在Y1，Y2两年之间的闰年总数。
print calendar.leapdays(1900, 2000)

i = datetime.datetime.now()
print ("当前的日期和时间是 %s" % i)
print ("ISO格式的日期和时间是 %s" % i.isoformat() )
print ("当前的年份是 %s" % i.year)
print ("当前的月份是 %s" % i.month)
print ("当前的日期是  %s" % i.day)
print ("dd/mm/yyyy 格式是  %s/%s/%s" % (i.day, i.month, i.year) )
print ("当前小时是 %s" % i.hour)
print ("当前分钟是 %s" % i.minute)
print ("当前秒是  %s" % i.second)






