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

distance = 20

class transport():
  """docstring for transport"""
  def __init__(self, kind, date):
    self.kind = kind
    self.date = date
  
  def maicai(self, time):
    speed = distance / time
    print '%s的时候骑%s去买菜，骑了%s小时,平均速度%s' %(self.date, self.kind, time, speed )

def main():
  
  day1 = transport("电动车", '周一')
  day2 = transport('自行车', '周二')
  day3 = transport('电动车', '周三')

  day1.maicai(0.5)
  day2.maicai(2)
  day3.maicai(0.6)



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
