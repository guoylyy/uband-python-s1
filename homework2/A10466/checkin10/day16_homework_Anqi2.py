#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import time

def main():
  ticks=time.time()
  print ticks
  localtime=time.asctime(time.localtime(time.time()))
  print localtime
  print time.strftime("%Y-%m-%d%H:%M:%S",time.localtime())
  import calendar
  cal=calendar.month(2017,6)
  print cal
  print calendar.isleap(2017)




if __name__ == '__main__':
  main()