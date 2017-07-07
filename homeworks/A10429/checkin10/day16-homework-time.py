#/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Irene
def main():
	import time
	ticks = time.time()
	print "时间： ", ticks

	localtime = time.localtime(time.time())
	print "本地时间为 :", localtime

	localtime = time.asctime( time.localtime(time.time()) )
	print "本地时间为 :", localtime

	print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

	print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime())

	a = "Tue Jun 20 21:11:03 2017"
	print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

	import calendar

	cal = calendar.month(2017, 6)
	print "以下输出2017年6月份的日历:"
	print cal;
if __name__ == '__main__':
	main()
