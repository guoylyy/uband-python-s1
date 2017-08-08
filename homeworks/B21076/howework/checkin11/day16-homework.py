#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: mansur
import turtle

# def main():
# 	windows=turtle.Screen()
# 	windows.bgcolor('red')
# 	bran=turtle.Turtle()
# 	bran.shape('turtle')
# 	bran.color('yellow')
# 	for i in range(1,10):
# 		bran.speed(1)
# 		bran.forward(100)
# 		bran.right(90)
# 		bran.forward(150)
# 		bran.right(90)
# 		bran.forward(100)
# 		bran.right(90)

import time
import calendar
def timeTest():
	ticks=time.time()
	print "now time is: ",ticks
	localtime=time.localtime(time.time())
	print "local time is: ",localtime
	print "local time is: ",time.asctime(localtime)
	print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())

def calendarTest():
	cal=calendar.month(2016,1)
	print "以下输出2016年1月份的日历："
	print cal


if __name__ == '__main__':
  # main()
  timeTest()
  calendarTest()