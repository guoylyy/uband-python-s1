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
class bike():
  def __init__(self, style, hour):
    self.style = style
    self.hour = hour
    self.speed = 20/self.hour

  def ride(self, date):
    self.date = date
    print "%s 骑 %s 平均时速 %0.2f km/h" %(self.date, self.style, self.speed)

def main():
  
  bike1 = bike("电动车",0.5)
  bike1.ride("周一")
  bike2 = bike("自行车",2)
  bike2.ride("周二")
  bike3 = bike("电动车",0.6) 
  bike3.ride("周三")
  
 

if __name__ == '__main__':
  main()
