#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Qipajie


import turtle

def homework1():

	windows=turtle.Screen()#后面忘+（） 换成小写无法运行

	windows.bgcolor('pink')

	bran=turtle.Turtle()   #中间是=    Q1:2个turtle Q2：bran的含义    调用右边的这个库，左边给它进行定义
							#A:有Turtle这个类，通过这个类实例化了一个叫做bran的小乌龟 
	bran.shape('turtle')
	bran.color('blue')

	bran.speed(1)


	for i in range(1,20):#后面是range
		bran.forward(100)  #bran常写成ban
		bran.left(45)
		bran.forward(100)
		bran.left(45)
		bran.forward(100)
		bran.left(45)



def homework2():
	import time
	#时间戳
	ticks=time.time()
	print "当前时间戳为:", ticks

	#当前时间
	localtime=time.localtime(time.time())
	print '当前时间为：',localtime

	#格式化时间
	localtime=time.asctime(time.localtime(time.time()))#local前忘+time   套几次就有几次time
	print '当前时间为：',localtime

	#格式化成特定形式strftime
	# 1)格式化成2016-03-20 11:45:39形式
	print time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime())   #%在数字前   忘了加''   localtime后忘加（）

	# 格式化成Sat Mar 28 22:24:24 2016形式
	print time.strftime('%a %b %d %H:%M:%S %Y',time.localtime())
	print time.strftime('%A %B %d %H:%M:%S %Y',time.localtime())
	# %a 本地简化星期名称   %A 本地完整星期名称——英文全称    
	#  %b 本地简化的月份名称  %B 本地完整的月份名称

	# 将格式字符串转换为时间戳
	a='2017-06-20 14:03:41'
	print time.mktime(time.strptime(a,'%Y-%m-%d %H:%M:%S'))   #mktime前有time.   是strpt  是p不是f
	#两个是相反的，strftime是将时间格式化，而strptime是转为时间戳  
	 #mktime表示转回时间戳

	#获取某月日历
	import calendar
	cal=calendar.month(2017,6) #后面缺了month  没有year的语法
	print  '下面输出2017年6月的日历'
	print cal
	

if __name__ == '__main__':
	homework1()
	homework2()
