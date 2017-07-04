#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import turtle

def main():
 
  windows = turtle.Screen()
  
  windows.bgcolor('yellow')
 
  ninjia = turtle.Turtle()
  ninjia.shape('turtle')
  ninjia.color('black')
  ninjia.dot(5,'red')

  for i in range(1,10):
    ninjia.fd(100)
    ninjia.right(144)


if __name__ == '__main__':
  main()

import time
import calendar
localtime = time.localtime()
local_time = time.asctime(localtime)

print time.strftime('%H:%M:%S %Y-%m-%d', time.localtime())
print time.strftime('%I:%M:%S %y-%m-%d', time.localtime())
print local_time

cal = calendar.month(2017,7)

print cal