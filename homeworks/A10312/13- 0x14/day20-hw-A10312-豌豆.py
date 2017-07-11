#!/usr/bin/python
# -*- coding: utf-8 -*-
#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度


class Bicycle():
  def __init__(self, name, hour, date):
    self.name = name
    self.hour = hour
    self.date = date

  def speed(self, distance):
    speed = float(distance)/self.hour
    print '%s 老妈 骑了%s 去菜场买菜 平均速度 %f km/h' % (self.date, self.name, speed)

def main():
  E_Bicycle1 = Bicycle('电动车',0.5,'周一')
  E_Bicycle1.speed(20)

  Bicycle1 = Bicycle('自行车',2,'周二')
  Bicycle1.speed(20)

  E_Bicycle2 = Bicycle('电动车',0.6,'周三')
  E_Bicycle2.speed(20)




  



if __name__ == '__main__':
  main()
