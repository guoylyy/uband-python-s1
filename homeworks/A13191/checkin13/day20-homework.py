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

class Vehicle():
	def __init__(self, kind):
		self.kind=kind

	def grocery_v(self, time, date):
		v=20/time
		print '%s骑%s平均时速%0.2fkm/h'%(date, self.kind, v)


def main():
  veh1=Vehicle('电动车')
  veh2=Vehicle('自行车')

  veh1.grocery_v(0.5, '周一')
  veh2.grocery_v(2,'周二')
  veh1.grocery_v(0.6,'周三')


if __name__ == '__main__':
  main()
