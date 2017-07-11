
# -*- coding: utf-8 -*-
# author: shuan


#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度

class ride():
  def __init__(self, name, date):

    self.name = name
    self.date = date

  def speed(self, distance, time):

    self.distance = distance
    self.time = time
    speed = distance / time
    print '%s老妈骑%s，平均时速为%dkm/h'%(self.date, self.name, speed)

def  main():
  distance = 20

  monday = ride('电动车', '周一')
  monday.speed(20, 0.5)

  Tuesday = ride('自行车', '周二')
  Tuesday.speed(20, 2)

  Wednesday = ride('电动车', '周三')
  Wednesday.speed(20, 0.6)

if __name__ == '__main__':
  main()