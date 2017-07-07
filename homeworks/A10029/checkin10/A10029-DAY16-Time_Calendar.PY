#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zi le

def time():

	import time#引入time

	#时间戳
	ticks=time.time()
	print '当前时间戳为： ',ticks

	#时间戳转化为时间元组
	localtime=time.localtime(time.time())
	print '本地时间： ',localtime

	#获取格式化时间
	localtime=time.asctime(time.localtime(time.time()))
	print '本地时间为： ',localtime

	#格式化为2017-06-20 10:52:44形式
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
	#%y 两位数的年份表示（00-99）%Y 四位数的年份表示（000-9999）
	#%m 月份（01-12）%d 月内中的一天（0-31）
	#%H 24小时制小时数（0-23）%I 12小时制小时数（01-12）
	#%M 分钟数（00=59）%S 秒（00-59）

	#格式化为Tue Jun 20 10:52:36 2017形式
	print time.strftime('%a %b %d %H:%M:%S %Y',time.localtime())
	#%a 本地简化星期名称%A 本地完整星期名称 %b 本地简化的月份名称 %B 本地完整的月份名称
	#

	#将格式字符串转化为时间戳
	a='Tue Jun 20 10:52:44 2017'
	print time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y'))

def calendar():

	import calendar#引入calender

	#获取某月日历
	cal=calendar.month(2017,1)
	print '以下输出2017年1月的日历 '
	print cal

	#判断是否为闰年
	print calendar.isleap(2016)
	print calendar.isleap(2017)

	#获取某年日历
	print calendar.calendar(2017,w=2,l=1,c=6)






if __name__=='__main__':
	time(),calendar()
