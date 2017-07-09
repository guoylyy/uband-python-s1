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



class day():
  def __init__(date,week,tool):
  	date.week = week
  	date.tool = tool 

  def average_speed(date,time):
  	distance = 20
  	average_speed = distance/ float(time)
  	print '%s 的时候老妈骑着 %s去买菜，骑了 %g 小时，平均速度为 %g 公里/小时 ' % (date.week, date.tool, time, average_speed)
def main():
   Mon = day('周一 ', '电动车')
   Mon.average_speed(0.5)
   Tue = day('周二 ', '自行车 ')
   Tue.average_speed(2)
   Wed = day('周三 ', '电动车')
   Wed.average_speed(0.6)#!/usr/bin/python


if __name__ == '__main__':
  main()



