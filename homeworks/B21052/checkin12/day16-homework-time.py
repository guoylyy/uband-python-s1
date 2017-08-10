#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: caramel
import time   #引入time模块

#获取当前时间戳，从1970年1月1日午夜（历元）经过了多长时间来表示
ticks = time.time()
print '当前时间戳为:', ticks

#获取时间元组（当地时间）
localtime = time.localtime(time.time())
print '本地时间为 ：', localtime

#获取格式化的时间
localtime = time.asctime(time.localtime(time.time()))
print '本地时间为：', localtime


#格式化日期，用 time 模块的 strftime 方法来格式化日期
#格式化成2016-03-20 11:45:39形式
print time.strftime('%Y-%m-%d %H:%M%S:', time.localtime())
# 格式化成Sat Mar 28 22:24:24 2016形式
print time.strftime('%a %b %d %H:%M:%S %Y', time.localtime())
# 将格式字符串转换为时间戳
a = 'Sat Mar 28 22:24:24 2016'
print time.mktime(time.strptime(a, '%a %b %d %H:%M:%S %Y'))
