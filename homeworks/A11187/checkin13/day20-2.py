#!/usr/bin/python
# -*- coding: utf-8 -*-

class Day():
	def __init__(self, datetime, hour):
		self.datetime = datetime
		self.hour = hour
 
	def be_drived(self, vehicle):
		distance = 20
		speed = distance/self.hour
		print 'mother on %s drives %s, the average speed is %0.2f km/h.' % (self.datetime, vehicle, speed)

def main():
	vehicle1 = 'e_bicycle'
	vehicle2 = 'bicycle'

	day1 = Day('Monday', 0.5)
	day1.be_drived(vehicle1)

	day2 = Day('Tuesday', 2)
	day2.be_drived(vehicle2)

	day3 = Day('Wednesday', 0.6)
	day3.be_drived(vehicle1)

if __name__ == '__main__':
	main()