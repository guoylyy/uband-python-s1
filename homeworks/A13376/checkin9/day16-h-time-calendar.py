#!/usr/bin/python
# -*- coding: utf-8 -*-

import time

localtime = time.asctime(time.localtime(time.time()))
print '本地时间为:' , localtime

import calendar
cal = calendar.month(2017,6)
print '以下输出2017年6月的日历:'
print cal;
