#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: luwei

import time

def main():
  #时间戳
  ticks = time.time()
  print ticks

  #获取当前时间
  localtime = time.localtime(time.time())
  print localtime

  #获取格式化的时间 #可读时间模式
  localtime = time.asctime(time.localtime(time.time()))
  print localtime

  #格式化日期
  #time.strftime(format[,t])
  #格式化成2016-03-20 11:45:39形式
  print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  #格式化成Sat Mar 28 22:24:24 2016形式
  print time.strftime("%a %b %d %H:%M:%S %Y",time.localtime())
  # 将格式字符串转换为时间戳
  a = "Tue Jun 20 11:06:15 2017"
  print time.mktime(time.strptime(a,"%a %b %d %H:%M:%S %Y"))

if __name__ == '__main__':
  main()

import calendar

cal = calendar.month(2017,6)
print cal



