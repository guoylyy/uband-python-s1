#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: bettyyan
import time
import calendar

def main():
  # 时间戳
  ticks = time.time()
  print 'now is:',ticks
  # 获取当前时间
  localtime = time.localtime(time.time())
  print 'local time is:',localtime
  # 获取格式化的时间
  localtime1 = time.asctime(time.localtime(time.time()))
  print 'local time is:',localtime1
  # 格式化日期
  # 格式化成2016-03-20 11:45:39形式
  print time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
  # 格式化成Sat Mar 28 22:24:24 2016形式
  print time.strftime('%a %b %d %H:%M:%S %Y',time.localtime())
  # 将格式字符串转换为时间戳
  a = "Sat Mar 28 22:24:24 2016"
  print time.mktime(time.strptime(a,'%a %b %d %H:%M:%S %Y'))

  #获取日历
  cal = calendar.month(2017,6)
  print 'it is the calendar of June 2017:'
  print cal;


if __name__ == '__main__':
  main()