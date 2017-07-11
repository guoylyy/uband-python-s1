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

class ride():
  """docstring for ride"""
  def __init__(self, day, hour):    
    self.day = day
    self.hour = hour    

  def speed(self,distance,vehicle):
    speed = float(distance)/self.hour
    print '%s 的时候骑%s，平均时速 %0.2f km/h' %(self.day,vehicle,speed)

def main():
  Mon = ride('周一',0.5) #这次的错误在于，''也不要乱加，一不小心就把数字变成了字符
  Mon.speed(20,'电动车')
  Tue = ride('周二',2)
  Tue.speed(20,'自行车')
  Wed = ride('周三', 0.6)
  Wed.speed(20,'电动车')
# 


if __name__ == '__main__':
  main()
    

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


# if __name__ == '__main__':
#   main()
