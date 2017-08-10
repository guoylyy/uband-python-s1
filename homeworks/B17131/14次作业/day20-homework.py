#!/usr/bin/python
# -*- coding: utf-8 -*-
# 什么是面向对象
#把我给的一段面向过程的代码修改成面向对象的方式，截图打卡
#思考一下面向对象的意义和价值，不用打卡: 我觉得面向对象还是比面向过程其实更省力简便吧，省去很多不必要打的代码，把力气花在问题的核心上，剩下的交给电脑程序解决。


#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度
def main():
  distance = 20

  e_bicycle = '电动车'
  bicycle = '自行车'

  day1 = '周一'
  hour1 = 0.5
  speed1 = 20/hour1
  print '%s 骑 %s 平均时速 %0.2f km/h' %(day1,e_bicycle, speed1)

  day2 = '周二'
  hour2 = 2
  speed2 = 20/hour2
  print '%s 骑 %s 平均时速 %0.2f km/h' %(day2,bicycle,speed2)

  day3 = '周三'
  hour3 = 0.6
  speed3 = 20/hour3
  print '%s 骑 %s 平均时速 %0.2f km/h' %(day3, e_bicycle, speed3)


if __name__ == '__main__':
  main()



#!/usr/bin/python
# -*- coding: utf-8 -*-

class Vehicle():
  def __init__(self,type,hour,day):
    self.type = type
    self.hour = hour
    self.day = day

  def be_rode(self):
    who = '妈妈'
    speed = 20/self.hour
    print '%s, %s骑%s去菜场卖菜，平均时速%0.2f km/h' %(self.day,who,self.type, speed)

def main():
  vehicle1 = Vehicle('电动车',0.5,'周一')
  vehicle1.be_rode()

  vehicle2 = Vehicle('自行车',2,'周二')
  vehicle2.be_rode()

  vehicle3 = Vehicle('电动车',0.6,'周三')
  vehicle3.be_rode()

if __name__ == '__main__':
  main()

  #周一, 妈妈骑电动车去菜场卖菜，平均时速40.00 km/h
  #周二, 妈妈骑自行车去菜场卖菜，平均时速10.00 km/h
  #周三, 妈妈骑电动车去菜场卖菜，平均时速33.33 km/h
    

