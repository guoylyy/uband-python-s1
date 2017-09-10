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
  """docstring for bike"""
  def __init__(self, ride_class,ride_time):
    self.ride_class=ride_class
    self.ride_time = ride_time
  def be_ride(self,weekday,distance):
    speed=float(distance)/self.ride_time
    print "%s的时候骑%s,平均时速为%0.2f km/h"%(weekday,self.ride_class,speed)
 
def main():
  lst1=['周一',"周二","周三"]
  lst2=['电动车','自行车','电动车']
  lst3=[0.5,2,0.6]
  distance=20
  for (i,l,m) in zip(lst1,lst2,lst3): #同时遍历多个列表，可以使用zip命令

  
    bike1=Bike(l,m)  
    
    bike1.be_ride(i,distance)  


  
if __name__ == '__main__':
  main()
