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
  def __init__(self,type,date,speed):
    self.type = type
    self.date = date
    self.speed = speed

  def be_rode(self,distance):
    hour = float(distance)/self.speed
    print '%s 骑 %s 平均时速 %0.2f km/h' %(self.date,self.type,hour) 
    

def main():
  bicycle = Bicycle('电动车','周一',0.5)
  bicycle.be_rode(20)

  bicycle2 = Bicycle('自行车','周二',2)
  bicycle2.be_rode(20)

  bicycle3 = Bicycle('电动车','周三',0.6)
  bicycle3.be_rode(20)
  
  


if __name__ == '__main__':
  main()
