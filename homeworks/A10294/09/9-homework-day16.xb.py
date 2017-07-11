#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xb

import time;
def main():
  ticks = time.time()
  print '当前时间戳为：', ticks

  localtime = time.localtime(time.time())
  print '本地时间：', localtime
  
  localtime = time.asctime(time.localtime(time.time()))
  print '本地时间：', localtime

  print time.strftime('%y-%m-%d %H:%M:%S', time.localtime())
  print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 


def main2():
  import calendar
  cal = calendar.month(2017, 6)
  print "输出六月日历"
  print cal;





if __name__ == '__main__':
  main(), main2()