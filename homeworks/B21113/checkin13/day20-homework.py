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
def main():
  distance = 20

  e_bicycle = '电动车'
  bicycle = '自行车'

  day1 = '周一'
  hour1 = 0.5
  speed1 = 20/hour1
  print '%s 骑 %s 平均时速 %0.2f km/h' %(day1,e_bicycle, speed1)

  day2 = '周二'
  hour2 = 2
  speed2 = 20/hour2
  print '%s 骑 %s 平均时速 %0.2f km/h' %(day2,bicycle,speed2)

  day3 = '周三'
  hour3 = 0.6
  speed3 = 20/hour3
  print '%s 骑 %s 平均时速 %0.2f km/h' %(day3, e_bicycle, speed3)

  print '--------------------------------'



class Cycle():
  def __init__(self, type, date,hour):
    self.type = type
    self.date = date
    self.hour = hour
   
  def be_rided(self):
  	speed = 20/self.hour
  	print '老妈 %s 骑 %s 平均时速 %0.2f km/h' %(self.date, self.type, speed)

def main1():
  cycle1 = Cycle('电动车','星期一',0.5)
  cycle1.be_rided()

  cycle2 = Cycle('自行车','星期二',2)
  cycle2.be_rided()

  cycle3 = Cycle('电动车','星期三',0.6)
  cycle3.be_rided()


if __name__ == '__main__':
  main()
  main1()
