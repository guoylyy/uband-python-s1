#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yan

import turtle
import time
import calendar

def main():
	windows = turtle.Screen()
	windows.bgcolor('pink')

	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')

	bran.speed(1)
	for i in range(1,10):
		bran.forward(100)
		bran.right(60)
		bran.forward(100)
		bran.right(60)
		bran.forward(100)
		bran.right(60)
		bran.forward(100)
		bran.right(60)
		bran.forward(100)
		bran.right(60)
		bran.forward(100)
		bran.right(60)

def try_time():
	ticks = time.time()
	print '时间戳为',ticks
	localtime = time.localtime(time.time())
	print 'localtime:',localtime
	localtime = time.asctime(time.localtime(time.time()))
	print 'localtime2:',localtime
	print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
	print time.strftime('%A %B %d %H:%M:%S %Y',time.localtime())
	a = 'Tue Jul 25 12:48:15 2017'
	print time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y'))

def try_calendar():
	cal = calendar.month(2017,7)
	print cal
	print calendar.isleap(2017)
	print calendar.leapdays(1997,2017)

if __name__ == '__main__':
	main()
	try_time()
	try_calendar()