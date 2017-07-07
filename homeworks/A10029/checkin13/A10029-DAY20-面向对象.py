#!/usr/bin/python
# -*- coding: utf-8 -*-
#@author: zi le
# 什么是面向对象


#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度
class tronsportation():
  def __init__(self,name):
    self.name=name

  def week(self,week):
    print '今天%s ，老妈骑 %s 去买菜 '%(week,self.name)
  
  def time(self,distance,hour):
    speed=distance/hour
    print ' 平均时速 %0.2f km/h '%(speed)

def main():
  day1=tronsportation(' 电动车 ')
  day1.week(' 周一 ')
  day1.time(20,0.5)

  day2=tronsportation(' 自行车 ')
  day2.week(' 周二 ')
  day2.time(20,2)

  day3=tronsportation(' 电动车 ')
  day2.week(' 周三 ')
  day3.time(20,0.6)
  # distance = 20
  # e_bicycle = '电动车'
  # bicycle = '自行车'
  # day1 = '周一'
  # hour1 = 0.5
  # speed1 = 20/hour1
  # print '%s 骑 %s 平均时速 %0.2f km/h' %(day1,e_bicycle, speed1)
  # day2 = '周二'
  # hour2 = 2
  # speed2 = 20/hour2
  # print '%s 骑 %s 平均时速 %0.2f km/h' %(day2,bicycle,speed2)
  # day3 = '周三'
  # hour3 = 0.6
  # speed3 = 20/hour3
  # print '%s 骑 %s 平均时速 %0.2f km/h' %(day3, e_bicycle, speed3)


if __name__ == '__main__':
  main()
