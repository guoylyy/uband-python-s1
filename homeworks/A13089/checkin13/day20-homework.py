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

class Bicycle():
  def __init__(self, kind):
    self.kind = kind   #自身属性

  def ride(self,hour,date):   #可变的条件
    distance = 20
    speed=float(distance)/hour
    print '%s 骑 %s 平均时速 %0.2f km/h' %(date,self.kind,speed)

def main():
  
  e_bicycle1 = Bicycle('电动车')
  e_bicycle1.ride(0.5,'周一')

  bicycle2 = Bicycle('自行车')
  bicycle2.ride(2,'周二')

  e_bicycle3 = Bicycle('电动车')
  e_bicycle3.ride(0.6,'周三')

if __name__ == '__main__':
  main()
