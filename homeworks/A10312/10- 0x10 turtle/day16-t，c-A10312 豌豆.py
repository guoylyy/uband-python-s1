#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: wandou

import time

def main():
	ticks = time.time()
	print (" time now ", ticks)

	print '---'
	localtime = time.localtime(time.time())
	print ('local time is:',localtime)

import calendar
def main2():
	cal = calendar.month(2017,2)
	print ('canlendar of Feb,2017:')
	print (cal)


if __name__ == '__main__':
  main()
  main2()