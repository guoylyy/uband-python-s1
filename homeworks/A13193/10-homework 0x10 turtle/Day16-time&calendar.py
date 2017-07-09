#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Pennsylvania

import time

print time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())

localtime = time.asctime(time.localtime(time.time()))
print '本地时间为 ：', localtime


import calendar
cal = calendar.month(2017, 6)
print '============'
print '以下为2017年6月份的日历：'
print cal;