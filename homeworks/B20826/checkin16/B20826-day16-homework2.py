#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Casey


import time
ticks = time.time()
print "time:", ticks

localtime = time.localtime(time.time())
print "localtime:", localtime

localtime = time.asctime(time.localtime(time.time()))
print "localtime:", localtime

import calendar
cal = calendar.month(2017,6)
print "2017.6"
print cal;