#!/usr/bin/python
# -*- coding: utf-8 -*-

def time():
	import time
	ticks = time.time()
	print "当前时间戳为:", ticks

	localtime = time.localtime(time.time())
	print "本地时间为 :", localtime

	localtime = time.asctime( time.localtime(time.time()) )
	print "本地时间为 :", localtime

	print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
	
if __name__ == '__main__':
	time()