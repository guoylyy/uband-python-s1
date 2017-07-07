#!/usr/bin/python
# -*- coding: utf-8 -*-
# 什么是面向对象

class Car():
	def __init__(self, brand, hour):
	 self.brand = brand
	 self.hour = hour

	def day(self, day):
		distance = 20
		speed = float(distance)/self.hour
		print '老妈 %s 骑 %s 平均时速 %0.2f km/h' %(day, self.brand, speed)

def main():
	car1 = Car('e_bicycle', 0.5)
	car1.day('周一')

	car2 = Car('bicycle', 2)
	car2.day('周二')

	car3 = Car('e_bicycle', 0.6)
	car3.day('周三')


if __name__ == '__main__':
  main()