#! usr/bin/python
# -*- coding: utf-8 -*-
# @author:Emma

class Drive():
	def __init__(self,brand,hour,day):
		self.brand = brand
		self.hour = hour
		self.day = day
	def be_dirved(self,distance):
		speed = float(distance)/self.hour
		print '%s 骑 %s 平均时速 %0.2f km/h' %(self.day,self.brand,speed)

def main():
	drive1 = Drive('电动车',0.5,'周一')
	drive1.be_dirved(20)

	drive2 = Drive('自行车',2,'周二')
	drive2.be_dirved(20)

	drive3 = Drive('电动车',0.6,'周三')
	drive3.be_dirved(20)
	
if __name__ == '__main__':
	main()