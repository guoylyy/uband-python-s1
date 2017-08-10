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
class transport(object):
   """docstring for transprot"""
   def __init__(self, name,hour,day):
     self.name = name
     self.hour = hour
     self.day = day

   def speed(self):
     speed = 20/ self.hour
     print '%s骑 %s 平均时速 %0.2f km/h' % (self.day,self.name,speed)
      
def main():
  distance = 20
  e_bicycle = '电动车'
  bicycle = '自行车'
  day1 = transport(e_bicycle,0.5,'周一')
  day1.speed()
  day2 = transport(bicycle,2,'周二')
  day2.speed()
  day3 = transport(e_bicycle,0.6,'周三')
  day3.speed()
  


if __name__ == '__main__':
  main()
