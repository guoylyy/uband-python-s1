#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

class day():
	"""docstring for day"""
	def __init__(self, day, time):
		self.day = day
		self.time = time

	def speed(self, distance,vehicle):
		speed = float(distance)/self.time
		print '------------------'
		print '%s骑%s去买菜，骑了 %s 小时，平均速度 %s km/h'%(self.day, vehicle, self.time, speed)

def main():
	distance = 20
	e_bicycle = '电动车'
	bicycle = '自行车'

	day1 = day('周一', 0.5)
	day1.speed(distance, e_bicycle)

	day2 = day('周二', 2)
	day2.speed(distance, bicycle)

	day3 = day('周三', 0.6)
	day3.speed(distance, e_bicycle)


if __name__ == '__main__':
	main()



		
		
