#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: caramel
#什么是面向对象

class Vehicle():
	def __init__(self, day, kind):
		self.day = day
		self.kind = kind

	def be_drived(self, distance, hour):
		self.distance = distance
		self.hour = hour
		speed = float(distance)/float(self.hour)
		print '%s, my mother went to buy vegetable by %s, and the speed was %0.2f km/h.'% (self.day, self.kind, speed)


def main():

	vehicle_1 = Vehicle('Monday', 'electrombike')
	vehicle_1.be_drived(20, 0.5)

	vehicle_2 = Vehicle('Tuesday', 'bike')
	vehicle_2.be_drived(20,2)

	vehicle_3 = Vehicle('Wednesday', 'electrombike')
	vehicle_3.be_drived(20, 0.6)


if __name__ == '__main__':
  main()
