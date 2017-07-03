#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: shangxindepidan

import time # 引入time模块

def time_():
  ticks = time.time()
  print '当前时间戳：', ticks

  localtime = time.localtime(time.time())
  print '本地时间： ', localtime  # struct_time元组 ## tm_wday 0到6(0是周一)

  localtime2 = time.asctime(time.localtime(time.time()))  #即localtime2 = time.asctime(localtime)
  print '本地时间#time.asctime()#：', localtime2  # 获取格式化的时间

  # 格式化成20XX-XX-XX XX:XX:XX形式   #time.strftime()
  print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  # 格式化成W M D XX:XX:XX Y形式
  print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())  # %a for weekday; %b for month

  # 将格式化字符串转换为时间戳  #time.mktime(tupletime) 接受时间元组并返回时间辍
  a = "Sat Mar 28 22:24:24 2016"
  struct_time3 = time.strptime(a, "%a %b %d %H:%M:%S %Y")  #time.strptime(string[, format])
  print struct_time3   # a的时间元组
  print time.mktime(struct_time3)  # a的时间戳

  # %y for simplified year   # %I for hour in 12-hour time system  
  # %c for XX/XX/XX(%x for date) + XX:XX:XX(%X for time)
  # %j for day number in a year     # %p for symbom AM or PM
  # %U for week number in a year(Sunday for start)  # %W for ... (Monday for start)
  # %w for day number in a week(0-6, Sunday as 0 as start)   # %% for mark % itself
  print time.strftime("%y %I %c %j %p %U %w %W %x %X %%", time.localtime())

  # print time.strftime("%Z", time.localtime())   ## %Z for current time zone; failed, can't run, pritn nothing
  print '---'  #内置函数
  print time.altzone # 返回格林威治西部的夏令时地区的偏移秒数。如果该地区在格林威治东部会返回负值（如西欧，包括英国）。对夏令时启用地区才能使用。
  print time.clock() # 用以浮点数计算的秒数返回当前的CPU时间。用来衡量不同程序的耗时，比time.time()更有用。
  print time.ctime() # 作用相当于asctime(localtime(secs))，未给参数相当于asctime()
  print time.gmtime() # 格林威治天文时间

  print 'Start:', time.ctime()
  time.sleep(5)  # time.sleep(t) t代表推迟执行的秒数
  print 'End:', time.ctime()
  print time.localtime()

  print time.timezone
  print time.tzname

  ## time.tzset() 太复杂，不懂

import calendar

def calendar_():
  cal = calendar.month(2017, 6)  # by default w=2 l=1
  print cal  # 2017年6月份日历

  print '--------------------'
  # calendar内置函数
  #calendar of year 2017: c=distance(month); l=line(week); w=distance(day)
  print calendar.calendar(2017, w=2, l=1, c=6)  #lenth(line)= 21* W+18+2* C

  print calendar.firstweekday() # start weekday, 0 by default, i.e. Monday
  # calendar.setfirstweekday(weekday)  # 0(Monday) to 6(Sunday)

  print calendar.isleap(2017) # return True or False
  print calendar.leapdays(2000, 2016) # number of leap years between year 1 and year 2

  print calendar.month(2017, 6)
  print calendar.monthcalendar(2017, 6)

  print calendar.monthrange(2017, 6)  # return (a, b)  a=starting weekday b=days in month

  calendar.prcal(2017, w=2, l=1, c=4)  # equals to print calendar.calendar(2017, w=2, l=1, c=4)
  calendar.prmonth(2017, 6) # equals to print calendar.month(2017, 6)

  print calendar.timegm(time.localtime()) #和time.gmtime相反：接受一个时间元组形式，返回该时刻的时间辍

  print calendar.weekday(2017, 6, 30) # calendar.weekday(year,month,day) return date code

if __name__ == '__main__':
  # time_()
  print '--------------------'
  calendar_()