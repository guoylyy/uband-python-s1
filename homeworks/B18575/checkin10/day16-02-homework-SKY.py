#! /bin/usr/python
#-*- coding:utf-8 -*-
#@author:SKY

import time
import calendar

def main():
	ticks=time.time()
	print ' 当前的时间戳： ',ticks

	localtime = time.localtime(ticks)
	print "本地时间为 :", localtime

	localtime1 = time.asctime(localtime)
	print "本地时间为 :", localtime1

	print time.strftime("%Y-%m-%d %H:%M:%S",localtime) 
	print time.strftime("%a %b %d %H:%M:%S %Y",localtime) 

	a = "Sat Mar 28 22:24:24 2016"
	print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

	cal = calendar.month(2017, 5)
	print "以下输出2017年5月份的日历:"
	print cal;

if __name__ == '__main__':
	main()