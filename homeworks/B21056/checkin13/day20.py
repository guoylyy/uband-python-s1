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
class Bicycle():
  def __init__(self,bicycle,day,hour):
    self.bicycle=bicycle
    self.day=day
    self.hour=hour
  
  def be_drived(self,distance):
    speed=distance/self.hour
    print '%s 骑 %s 平均时速 %0.2fkm/h'%(self.day,self.bicycle,speed)


def main():
  distance = 20

  bicycle1=Bicycle('电动车','周一',0.5)
  bicycle1.be_drived(distance)

  bicycle2=Bicycle('自行车','周二',2)
  bicycle2.be_drived(distance)

  bicycle3=Bicycle('电动车','周三',0.6)
  bicycle3.be_drived(distance)


if __name__ == '__main__':
  main()
