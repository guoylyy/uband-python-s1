#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: vera

class Buy():
	def __init__(self, day, vehicle):
		self.day = day
		self.vehicle = vehicle

	def go(self, hour):
		distance = 20 #km
		self.hour = hour
		speed = float(distance)/self.hour
		print 'On %s mom rides her %s and the speed is %0.2f km/h.' % (self.day, self.vehicle, speed)

def main():
	buy1 = Buy('Monday', 'motorbike')
	buy1.go(0.5)

	buy2 = Buy('Tuesday', 'bike')
	buy2.go(2)

	buy3 = Buy('Wendesday', 'motorbike')
	buy3.go(0.6)

if __name__ == '__main__':
	main()