#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yuanzi
# 什么是面向对象


#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度

class Bike():
  def __init__(self, bike, day):
  	self.bike = bike
  	self.day = day
  	

  def drive(self, distance, hour):

    distance = 20
    speed = distance/float(hour)
    print '老妈 %s 骑%s,平均时速 %0.2f km/h' %(self.day, self.bike, speed)

def main():
  bike1 = Bike('电动车','周一') 
  bike1.drive(20,0.5)	
  bike2 = Bike('自行车','周二')
  bike2.drive(20,2)
  bike3 = Bike('电动车','周三')
  bike3.drive(20,0.6)

if __name__ == '__main__':
	main()