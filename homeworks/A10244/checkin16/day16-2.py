#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:Muzi
import time,calendar,datetime
ticks=time.time()
print ticks
localtime=time.localtime(time.time())
print localtime
localtime2=time.asctime(time.localtime(time.time()))
print localtime2
print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
print time.strftime('%a-%b-%d %H:%M:%S',time.localtime())
cal=calendar.month(2017,7)
print cal
print '------------'
print calendar.calendar(2017)
print '-----------'
calendar.setfirstweekday(4)
print calendar.firstweekday()
i=datetime.datetime.now()
print i
print i.isoformat()
print i.year