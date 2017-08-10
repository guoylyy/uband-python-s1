#!/usr/bin/python
# -*- coding: utf-8 -*-

import turtle
import time
import calendar

def main1():
	#设置一个画面
	windows = turtle.Screen()

	#设置背景
	windows.bgcolor('pink')

	#生成一个白色乌龟
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('white')

	#设置速度
	bran.speed(1)

	#走几步
	for i in range(1,10):
		bran.forward(100)
		bran.right(90)
		bran.forward(100)
		bran.right(90)
		bran.forward(100)
		bran.right(90)
		bran.forward(100)
		bran.right(90)

def main2():
	#time 函数
	print "-------"
	tick=time.time()
	print "当前时间为",tick
	#localtime 函数
	print "-------"
	times=time.localtime(tick)
	print times
	print time.localtime()
	#格式化时间：asctime函数(已经给好格式)
	print "-------"
	time1=time.asctime(time.localtime())
	print time1
	#格式化日期：strftime函数（自己定义格式）
	print "-------"
	date1=time.strftime("%Y-%m-%d %W %H:%M:%S",times)
	print date1
	date2=time.strftime("%a %b %d %Y",times)
	print date2
	#将格式化的日期转换为时间戳: strptime函数 和 mktime函数
	print "-------"
	date3="Sat Mar 28 22:24:26 2017"
	a=time.strptime(date3,"%a %b %d %H:%M:%S %Y")
	print a
	date4=time.mktime(a)
	print date4
	#clock函数
	cputime=time.clock
	print time.clock()

def main3():

	#month函数
	print "-------"
	cal1 = calendar.month(2017,7)
	print cal1

	cal2 = calendar.monthcalendar(2017,1)
	print cal2



if __name__ == '__main__':
	main3()

