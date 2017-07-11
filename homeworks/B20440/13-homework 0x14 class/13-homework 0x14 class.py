#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tingting

class speed():
	def __init__(self, distance, time, vihicle, day):	
		self.distance = distance
		self.time = time
		self.vihicle = vihicle
		self.day = day
		
	def shopping(self):
		number = self.distance/self.time
		print '%s的时候老妈骑%s平均时速为%dkm/h' % (self.day, self.vihicle, number)
	
				
def main():
		wednesday = speed(20, 0.6,'自动车', '周三')
		wednesday.shopping()	     
if __name__ == '__main__':
	main()
