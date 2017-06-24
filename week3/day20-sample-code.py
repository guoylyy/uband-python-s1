#!/usr/bin/python
# -*- coding: utf-8 -*-
# 什么是面向对象

def main():
  car1 = "捷达"
  speed1 = 60 #km/h
  distance1 = 300 #km
  hour = distance1/speed1
  print '驾驶 %s 开 %dkm 去b地开了 %0.2f 小时' % (car1, distance1, hour)

  car2 = "捷豹"
  speed2 = 120 #km/h
  distance2 = 400 #km
  hour2 = float(distance2)/speed2
  print '驾驶 %s 开 %dkm 去b地开了 %0.2f 小时' % (car2, distance2, hour2)

if __name__ == '__main__':
  main()
