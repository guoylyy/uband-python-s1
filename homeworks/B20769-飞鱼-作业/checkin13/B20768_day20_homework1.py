#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B20769-feiyu
#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度

class Buy():
	def __init__(self, day, transport, time):
		self.day = day
		self.transport = transport
		self.time = time

	def go(self, distance):
		speed = float(distance)/self.time
		print '%s ,老妈骑着 %s 去买菜, 平均时速为 %0.2f km/h' % (self.day, self.transport, speed)

def main():
	buy1 = Buy('周一', '电动车', 0.5)
	buy1.go(20)
	buy2 = Buy('周二', '自行车', 2)
	buy2.go(20)
	buy3 = Buy('周三', '电动车', 0.6)
	buy3.go(20)

if __name__ == '__main__':
	main()