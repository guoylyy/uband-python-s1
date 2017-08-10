#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guo


def main():

	import time
	ticks=time.time()
	print ' 当前时间戳为：',ticks   
	print '---------'
	localtime=time.localtime(time.time())
	print ' 本地时间为：',localtime  
	print '---------'
	localtime=time.asctime(time.localtime(time.time()))
	print '本地时间为：',localtime
	print '---------'
	print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
	print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
	a=time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())
	print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))
	print '---------'


	import calendar
	cal=calendar.month(2017,7)
	print cal

if __name__ == '__main__':
    main()