#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

import calendar

cal = calendar.month(2017, 7)
print cal

cal_1 = calendar.calendar(2017)
#print cal_1

print calendar.isleap(2000)

print calendar.leapdays(2000,2017)

print calendar.monthcalendar(2017,7)

print calendar.monthrange(2017,7)

print calendar.weekday(2017,7,25)