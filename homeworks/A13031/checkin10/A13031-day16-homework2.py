#!/usr/bin/python
#	-*-	coding:	utf-8	-*-
#	@author:	xxx
import	time

print	'Time'
localtime	=	time.localtime(time.time())
print	'本地时间为：',localtime
print	'--------'
print	time.strftime("%Y-%m-%d	%H:%M:%S",	time.localtime())

print	'--------'
print	time.strftime("%a %b %d	%H:%M:%S %Y",	time.localtime())

print	'--------'
a	=	"Sat	Mar	28	22:24:24	2016"
print	time.mktime(time.strptime(a,"%a %b %d	%H:%M:%S %Y"))
print	'      '

print	'Calendar'
import	calendar

cal	=	calendar.month(2017,1)
print	"以下输出2016年1月份的日历："
print	cal;
