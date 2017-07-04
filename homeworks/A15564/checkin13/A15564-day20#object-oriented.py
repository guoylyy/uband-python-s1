#!/usr/bin/python
# -*- coding: utf-8 -*-
# 什么是面向对象
# @author: shangxindepidan


#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度

class Vehicle():
  def __init__(self, vehicle):
    self.vehicle = vehicle

  def show_vehicle(self):
    print 'Mom has a(n) %s.' %(self.vehicle)

  def gogo(self, weekday, hour, intention, distance):
    if intention:  # boolean: True=='buy'  False=='sell'
      print '%s, Mom drove her %s to the market for purchase, taking %g h, at an average speed of %0.2f km/h.' %(weekday, self.vehicle, hour, distance / hour)
    else:
      print '%s, Mom drove her %s to the market for sale, taking %g h, at average speed of %0.2f km/h.' %(weekday, self.vehicle, hour, distance / hour)

def main1():
  v1 = Vehicle('bicycle')
  v2 = Vehicle('electric vehicle')
  v1.show_vehicle()
  v2.show_vehicle()
  distance = 20
  print 'The market is %d km away from home.' %(distance)
  v2.gogo('Monday', 0.5, True, distance)
  v1.gogo('Tuesday', 2, False, distance)
  v2.gogo('Wednesday', 0.6, False, distance)

if __name__ == '__main__':
  print '#main1(): class Vehicle'
  main1()

print '---'

class Weekday():
  def __init__(self, weekday, hour, intention):
    self.weekday = weekday
    self.hour = hour
    self.intention = intention

  def gogo2(self, vehicle, distance):
    if self.intention:  # boolean: True=='buy'  False=='sell'
      print '%s, Mom drove her %s to the market for purchase, taking %g h, at an average speed of %0.2f km/h.' %(self.weekday, vehicle, self.hour, distance / self.hour)
    else:
      print '%s, Mom drove her %s to the market for sale, taking %g h, at average speed of %0.2f km/h.' %(self.weekday, vehicle, self.hour, distance / self.hour)

def main2():
  day1 = Weekday('Monday', 0.5, True)
  day2 = Weekday('Tuesday', 2, False)
  day3 = Weekday('Wednesday', 0.6, False)
  v1 = 'bicycle'
  v2 = 'electric vehicle'
  print 'Mom has a %s and an %s.' %(v1, v2)
  distance = 20
  day1.gogo2(v2, distance)
  day2.gogo2(v1, distance)
  day3.gogo2(v2, distance)

if __name__ == '__main__':
  print '#main2(): class Weekday'
  main2()

