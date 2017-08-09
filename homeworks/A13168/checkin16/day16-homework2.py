#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import calendar

def main():
	cal = calendar.month(2017,7)
	print cal

import time

def main2():
	print time.strftime('%a %b %d %H:%M:%S %Y',time.localtime())
	print '-----'
	localtime = time.asctime( time.localtime(time.time()) )
	print '本地时间为：',localtime

if __name__ == '__main__':
	main()
	main2()
