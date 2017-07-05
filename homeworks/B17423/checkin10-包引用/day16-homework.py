#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: seiya
import turtle
import time;
import calendar

def homework2():
	ticks = time.time()
	print ('当前时间戳：', ticks)
	localtime = time.localtime(ticks)
	print ("本地时间：",localtime)
	asc_time = time.asctime(localtime)
	print ("格式化本地时间：",asc_time)

	f_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
	print ("格式化时间：",f_time)

	print (time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) ) #星期，月份，日

	# 将格式字符串转换为时间戳
	a = "Sat Mar 28 22:24:24 2017"
	print (time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y")))

	print ("---calendar---")
	cal = calendar.month(2017, 6)
	print (cal)


def main():
	#设置画面
	windows = turtle.Screen()
	#设置背景
	windows.bgcolor('red')
	#生成一个黄色乌龟
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')
	#设置速度
	bran.speed(2)

	#走几步
	for i in range(1,5):
		bran.forward(100)
		bran.right(90)
		bran.forward(150)
		bran.right(90)
		bran.forward(100)
		bran.right(90)
		bran.forward(150)
		bran.right(90)

if __name__ == '__main__':
	main()
	homework2()