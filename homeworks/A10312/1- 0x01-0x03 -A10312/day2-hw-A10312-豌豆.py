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
  def __init__(self, type, hour, date):
    self.type = type
    self.hour = hour
    self.date = date

  def be_drived(self, date, distance):
    speed = float(distance)/self.hour
    print '%g  %s 骑了 %dkm路 去菜场 花了 %f 小时 平均速度 %0.2h km/h' % (date, self.type,
       distance, hour, speed)

def main():
  E_Bicycle1 = Bicycle('电动车',0.5,'周一')
  E_Bicycle1.be_drived('周一',20)

  Bicycle = Bicycle('自行车',2,'周二')
  Bicycle.be_drived('周二',20)

  E_Bicycle2 = Bicycle('电动车',0.6,'周三')
  E_Bicycle2.be_drived('周三',20)




  



if __name__ == '__main__':
  main()
