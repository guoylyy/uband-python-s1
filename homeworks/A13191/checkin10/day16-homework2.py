#!/usr/bin/python
# -*- coding: UTF-8 -*-

import time
import calendar

print time.localtime()
print time.time()

localtime = time.localtime(time.time())
print "本地时间为:", localtime

localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为:", localtime

print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 

print '\n'

cal=calendar.month(2017,7)
print cal