#!/usr/bin/python
# -*- coding: utf-8 -*-
#Author: Pennsylvania
# 什么是面向对象


class tool(): 
  def __init__(self, tool, hours): 
    self.tool = tool 
    self.hours = hours 

  def week(self, week): 
    speed = 20/ self.hours 
    print '老妈 %s 骑 %s 平均速度 %0.2f km/h' %(week, self.tool, speed) 


def main(): 
  tool1 = tool('电动车', 0.5) 
  tool1.week('星期一') 

  tool2 = tool('自行车', 2) 
  tool2.week('星期二') 

  tool3 = tool('电动车', 0.6)
  tool3.week('星期三') 



if __name__ == '__main__':
  main()
