#!/usr/bin/python
# -*- coding: UTF-8 -*-  
# 
import time
import calendar

def main():
  #打印时间戳
  ticks = time.time()
  print "当前时间戳为:", ticks
  #打印本地时间
  localtime = time.localtime(time.time())
  print "本地时间为:",localtime
  #打印格式化时间
  print '------'
  localtime = time.asctime(time.localtime(time.time()))
  print "本地时间为：",localtime
  #其余格式时间表达
  print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
  print time.strftime("%a %b &d %H:%M:%S %Y,time.localtime()")


  #日历
  cal = calendar.month(2017,7)
  print '打印当月日历'
  print cal;
if __name__ == '__main__':
  main()