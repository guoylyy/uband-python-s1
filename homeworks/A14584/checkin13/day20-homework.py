#!/usr/bin/python
# -*- coding: utf-8 -*-
# 什么是面向对象
# @author: Chuan

#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度

class Cycle():
  def __init__(self, date, type, hour):
    self.date = date
    self.type = type
    self.hour = hour
  def be_rided(self):
    speed = 20/self.hour
    print '老妈%s 骑 %s 去菜场，用了%s小时，平均时速 %0.2f km/h' %(self.date, self.type, self.hour, speed)


def main():
  cycle1 = Cycle('周一','电动车',0.5)
  cycle1.be_rided()

  cycle2 = Cycle('周二','自行车',2)
  cycle2.be_rided()

  cycle3 = Cycle('周三','电动车',0.6)
  cycle3.be_rided()

if __name__ == '__main__':
  main()




  #distance = 20

  #e_bicycle = '电动车'
  #bicycle = '自行车'

  #day1 = '周一 '
  #hour1 = 0.5
  #speed1 = 20/hour1
  #print '%s 骑 %s 平均时速 %0.2f km/h' %(day1,e_bicycle, speed1)

  #day2 = '周二 '
  #hour2 = 2
  #speed2 = 20/hour2
  #print '%s 骑 %s 平均时速 %0.2f km/h' %(day2,bicycle,speed2)

  #day3 = '周三 '
  #hour3 = 0.6
  #speed3 = 20/hour3
  #print '%s 骑 %s 平均时速 %0.2f km/h' %(day3, e_bicycle, speed3)


#if __name__ == '__main__':
  #main()
