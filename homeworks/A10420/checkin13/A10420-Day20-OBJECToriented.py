# -*- coding: utf-8 -*-
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度

class Car():
	def __init__(self, name):
		self.name = name

	def speed(self, day, time):
		who = 'Mom'
		distance = 20
		speed = distance / time 
		print '%s, %s rides %s at speed of %d km/hr.' % (day, who, self.name, speed)

def main():
	motor = Car('motor')
	bicycle = Car('bicycle')

	motor.speed('Day1', 0.5)
	bicycle.speed('Day2', 2)
	motor.speed('Day3', 0.6)

if __name__ == '__main__':
	main()