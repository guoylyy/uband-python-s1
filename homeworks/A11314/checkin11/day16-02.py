#!/usr/bin/python
# coding:utf-8

import time,calendar,datetime

ticks = time.time()
print "当前时间戳为：%s"%(ticks)
localtime = time.localtime()
print localtime
localtime = time.asctime()
print localtime
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())

print time.mktime(time.strptime("Sat Mar 28 22:24:24 2016","%a %b %d %H:%M:%S %Y"))

print time.strftime("%y/%m/%d",time.localtime())
print time.strftime("%Y-%m-%d %A",time.localtime())
print time.strftime("%B,%c,%Z,%j",time.localtime())

cal = calendar.month(2017,7)
print cal

print calendar.calendar(2017,w=2,l=2,c=6)
print calendar.firstweekday()

print datetime.datetime.now()
time.sleep(0)
print time.clock()