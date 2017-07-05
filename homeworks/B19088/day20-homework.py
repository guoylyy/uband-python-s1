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

class Transportation():
  def __init__(self, type, hour):
   self.type = type
   self.hour = hour

  def avespeed(self,distance):
  
    speed = distance/self.hour
    print '老妈骑%s去买菜，平均速度是%d每小时' %(self.type, speed)

def main():
  day1 = Transportation('电动车',0.5)
  day1.avespeed(20)
  day2 = Transportation('自行车',2)
  day2.avespeed(20)
  day3 = Transportation('电动车',0.6)
  day3.avespeed(20)








if __name__ == '__main__':
  main()
