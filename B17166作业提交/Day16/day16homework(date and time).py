#!/usr/bin/python


import time
localtime = time.localtime(time.time())
print 'the local time :', localtime

print '---'

import time 
localtime=time.asctime(time.localtime(time.time()))
print 'the local time :',localtime

print '---'
import time
print time.strftime('%Y-%m-%d %H:%M:%S ',time.localtime())
print time.strftime('%a %b %d  %H:%M:%S %Y',time.localtime())

import calendar

cal = calendar.month(2017,6)
print 'this is the calendar of JUNE,2017'
print cal