#!/usr/bin/python
# -*- coding: utf-8 -*-

class tool():
  def __init__(self, tool, hour):
    self.tool = tool
    self.hour = hour
    

  def day(self, day, distance):
    speed = float(distance)/self.hour
    print'老妈%s 骑 %s 平均时速 %0.2f km/h' %(day, self.tool, speed)


def main():
  tool1 = tool('电动车', 0.5)
  tool1.day('星期一', 20)
  
  
  tool2 = tool('自行车', 2)
  tool2.day('星期二', 20)
 

  tool3 = tool('电动车', 0.6)
  tool3.day('星期三', 20)
 



if __name__ == '__main__':
  main()