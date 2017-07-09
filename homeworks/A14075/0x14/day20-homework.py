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
class record():
    def __init__ (self,date,vehicle,hour):
        self.date = date
        self.vehicle = vehicle
        self.hour = hour
        self.speed = distance / hour
    
    def output(self):
        print("%s 骑 %s 平均时速 %0.2f km/h"%(self.date,self.vehicle,self.speed))

def main():
  distance = 20

  e_bic= '电动车'
  bic = '自行车'
  day1 = record('周一',e_bic,0.5)
  day1.output()

  day2 = record('周二',bic,2)
  day2.output()

  day3 = record("周三",e_bic,0.6)
  day3.output()



if __name__ == '__main__':
    distance = 20
    main()
