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
class tool():
	def __init__(self, name):
		self.name = name
	
	def drive(self,day,hour):
		average_speed = 20/hour
		print '%s,mom drived %0.2f per hour.' %(day,average_speed)

def main():
	e_bicycle = tool('e_bicycle')
	e_bicycle.drive('Monday',0.5) 

	bike = tool('bike')
	bike.drive('Tuesday',2)

	e_bicycle = tool('e_bicycle')
	e_bicycle.drive('Wednesday',0.6) 

if __name__ == '__main__':
	main()