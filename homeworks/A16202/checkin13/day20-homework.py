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

# def main():
#   distance = 20

#   e_bicycle = '电动车'
#   bicycle = '自行车'

#   day1 = '周一'
#   hour1 = 0.5
#   speed1 = 20/hour1
#   print '%s 骑 %s 平均时速 %0.2f km/h' %(day1,e_bicycle, speed1)

#   day2 = '周二'
#   hour2 = 2
#   speed2 = 20/hour2
#   print '%s 骑 %s 平均时速 %0.2f km/h' %(day2,bicycle,speed2)

#   day3 = '周三'
#   hour3 = 0.6
#   speed3 = 20/hour3
#   print '%s 骑 %s 平均时速 %0.2f km/h' %(day3, e_bicycle, speed3)



class Buydish():
  def __init__(self,distance,day,tool):
    self.distance = distance
    self.day = day
    self.tool = tool

  def aver_speed(self,hour):
    speed = self.distance/hour
    print'老妈 %s 骑 %s 去买菜，平均时速 %0.2f km/h' %(self.day, self.tool, speed)

def main():
  buy1 = Buydish(20,'周一','电动车')
  buy1.aver_speed(0.5)

  buy2 = Buydish(20,'周二','自行车')
  buy2.aver_speed(2)

  buy3 = Buydish(20,'周三','电动车')
  buy3.aver_speed(0.6)

if __name__ =='__main__':
  main()

 
