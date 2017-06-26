# !/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Liluo   注释为第1题

# import turtle

# def main():
# 	windows=turtle.Screen()
# 	windows.bgcolor('green')

# 	tu=turtle.Turtle()
# 	tu.shape('turtle')
# 	tu.color('yellow')
# 	tu.speed(10)
# 	for i in range(1,10):
# 		tu.forward(100)
# 		tu.right(60)
# 		tu.forward(100)
# 		tu.right(60)
# 		tu.backward(100)
# 		tu.right(60)
import time
import calendar
def main():
	ticks=time.time()

	print "当前时间戳为：", ticks

	localtime=time.asctime(time.localtime(time.time()))
	print "localtime=", localtime

	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
	a = "Sat Mar 28 22:24:24 2016"
	print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))	
	cal=calendar.month(2017,7)
	print "日历"
	print cal
	print calendar.calendar(2015,w=2,l=1,c=6)

if __name__ == '__main__':
	main()