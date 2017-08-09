##!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

import time#这里后面可以加分号；也可以不加。
ticks=time.time()
print'the present 时间戳 is:',ticks#1970.1.1午夜至今经历过多长时间即为时间戳
localtime=time.localtime(time.time())#从返回浮点数的时间缀方式向时间元组转换，只要将浮点数传递给如Localtime之类的函数
print'本地时间为：',localtime
localtime2=time.asctime(time.localtime(time.time()))
print'本地时间为：',localtime2
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print time.strftime('%a %b %d %H:%M:%S %Y',time.localtime())
#将格式字串符转化为时间戳
a='Tue Jul 25 21:16:00 2017'
print time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y'))

import calendar
cal= calendar.month(2017,7)
print'以下输出2017年7月份的日历 '
print cal;

import datetime
i=datetime.datetime.now()
print('当前的日期和时间是%s'%i)
print('ISO格式的日期和时间是%s'%i.isoformat())
print('当前的年份是%s'%i.year)
print('当前的月份是%s'%i.month)
print('当前的日期是%s'%i.day)
print('dd/mm/yyy格式是 %s/%s/%s'%(i.day,i.month,i.year))
print('当前的小时是%s'%i.hour)
print('当前的分钟是%s'%i.minute)
print('当前的秒是%s'%i.second)