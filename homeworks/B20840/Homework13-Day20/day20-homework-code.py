#!/usr/bin/python
# -*- coding: utf-8 -*
#Author:B20840

class Auto(object):
	"""docstring for ClassName"""
	def __init__(self, brand, color, speed, weight):
		self.brand = brand
		self.color=color
		self.speed = speed
		self.weight = weight

	def be_drived(self, distance):
		hour = float(distance)/self.speed
		print '驾驶重达%s %s 色%s 开 %d 公里去B地 开了 %0.2f 小时' %(self.weight, self.color, 
			self.brand,distance, hour)

def main():
	car1 = Auto('捷达', '红',60, '2吨')		
	car1.be_drived(600)

if __name__ == '__main__':
	main()