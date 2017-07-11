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
class Vehicle():
  def __init__(self, kind, hour):

    self.kind = kind
    self.hour = hour
  

  def week(self,week):
    speed = 20/self.hour
    print '老妈周%s骑%s平均时速%0.2fkm/h' % (week, self.kind, speed)

def main():
  vehicle1 = Vehicle('电动车', 0.5)
  vehicle1.week('一')

  vehicle2 = Vehicle('自行车', 2)
  vehicle2.week('二')

  vehicle3 = Vehicle('电动车', 0.6)
  vehicle3.week('三')


if __name__ == '__main__':
  main()
