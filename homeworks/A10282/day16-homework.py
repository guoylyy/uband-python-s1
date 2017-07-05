#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: 233
import calendar
cal = calendar.month(2017, 1)
print '以下输出2017年1月份的日历：'
print cal;

print '-----------'
import time;
ticks = time.time()
print '当前时间戳为:', ticks

print '------------'
import time
localtime = time.localtime(time.time())
print '本地时间为:', localtime 
print '------------'
import time
localtime = time.asctime( time.localtime(time.time()))
print '本地时间为:', localtime 
  

 #引入库
import turtle
def main():
  
  windows = turtle.Screen()
  windows.bgcolor('red')
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('yellow')
  bran.speed(1)
  for i in range(1,10):
    bran.forward(100)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
    bran.forward(100)
    bran.right(90)
    bran.forward(150)
    bran.right(90)

  if __name__ == '__main__':
    main()
