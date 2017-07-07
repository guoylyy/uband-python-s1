#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author：SKY
# 什么是面向对象


#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度

#日常
class Day_to_day():
	def __init__(self,who):
		self.who=who

	def gotoMarket(self,when,how,why,costtime,distance):
		print ' %s%s的时候骑%s去%s, 骑了%0.2f小时, 速度为：%0.2f ' % (self.who,when,how,why,costtime,distance/costtime)

def main():
	mom=Day_to_day("老妈")
	distance = 20

	e_bicycle='电动车'
	bicycle='自行车'
	day1 = '周一'
	hour1 = 0.5
	mom.gotoMarket(day1,e_bicycle,"买菜",hour1,distance)
	# speed1 = 20/hour1
	# print '%s 骑 %s 平均时速 %0.2f km/h' %(day1,e_bicycle, speed1)
	day2 = '周二'
	hour2 = 2
	mom.gotoMarket(day2,bicycle,"卖菜",hour2,distance)
	# speed2 = 20/hour2
	# print '%s 骑 %s 平均时速 %0.2f km/h' %(day2,bicycle,speed2)

	day3 = '周三'
	hour3 = 0.6
	mom.gotoMarket(day3,e_bicycle,"卖菜",hour3,distance)
  # speed3 = 20/hour3
  # print '%s 骑 %s 平均时速 %0.2f km/h' %(day3, e_bicycle, speed3)


if __name__ == '__main__':
  main()
