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
class Bike():
  def __init__(self,day,kind,time):
    self.day=day
    self.kind = kind
    self.time = time

  def be_drived(self):
    distance=20
    speed = float(distance)/self.time
    print '在一周的%s，骑 %s 去买菜，去了%0.2f小时，平均速度是%0.2fkm/h ' % (self.day,self.kind,self.time,speed)

def main():
  bike1 = Bike('周一','电动车',0.5)
  bike1.be_drived()#这个括号一定要加，这样drive这个函数才能输出。

  bike1 = Bike('周二','自行车',2)
  bike1.be_drived()

  bike1 = Bike('周三','电动车',0.6)
  bike1.be_drived()

if __name__ == '__main__':
  main()
