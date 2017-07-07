#!/usr/bin/python
# -*- coding: utf-8 -*-
# 面向对象
# author:qianchang

#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度
distance = 20
who = '老妈'

class Vehicle ():
      def __init__(self, vehicle, date):
          self.vehicle = vehicle
          self.date = date
    
      def buy(self, time):
          speed = distance/time
          print '%s, %s 驾驶 %s 去买菜, 平均速度为%0.2f ' % (self.date, who, self.vehicle, speed)

vehicle1 = Vehicle ('电动车','周一')
vehicle2 = Vehicle ('自行车','周二')
vehicle3 = Vehicle ('电动车','周三')
vehicle1.buy(0.5)
vehicle2.buy(2)
vehicle3.buy(0.6)
