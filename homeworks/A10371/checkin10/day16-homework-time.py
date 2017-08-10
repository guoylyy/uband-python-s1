#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yuanzi
import time  #引入time模块

ticks = time.time()
print '当前时间戳为',ticks

#时间戳是自1970年1月1日（08:00:00GMT）至当前时间的总毫秒数。它也被称为Unix时间戳（UnixTimestamp）

localtime = time.localtime(time.time())
print '本地时间:',localtime

localtime = time.asctime(time.localtime(time.time()))
print '现在时间是',localtime

print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())
a = "Sat Mar 28 22:24:24 2016"
print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))