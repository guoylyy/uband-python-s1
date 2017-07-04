#!/usr/bin/python
# -*- coding: utf-8 -*-
# 什么是面向对象


#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度
class Che():
  def __init__(self, type, hour):
    self.type = type
    self.hour = hour

  def Speed(self, day, distance):
    self.distance = distance
    speed = distance/self.hour
    self.day = day
    print '%s 骑 %s 平均时速 %0.2f km/h' % (self.day,self.type, speed)

def main():
  e_bicycle = '电动车'
  bicycle = '自行车'
  distance = 20

  che1 = Che(e_bicycle, 0.5)
  che1.Speed('周一', distance)

  che1 = Che(bicycle, 2.0)
  che1.Speed('周二', distance)

  che1 = Che(e_bicycle, 0.6)
  che1.Speed('周三', distance)

if __name__ == '__main__':
  main()
