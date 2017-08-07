#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

import time


def main():
	ticks = time.time()
	print "now",ticks

	localtime = time.localtime(ticks)
	print localtime

	localtime_1 = time.asctime(localtime)
	print localtime_1

	print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

	print time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())

	a = "Tue Jul 25 17:12:53 2017" 
	print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))


if __name__ == '__main__':
	main()
