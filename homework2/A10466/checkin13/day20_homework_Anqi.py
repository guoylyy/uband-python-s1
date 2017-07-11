#!/usr/bin/python
# -*- coding: utf-8 -*-
class Car():
	def __init__(self, date, time, name):
		self.date = date
		self.time = time
		self.name = name
	def be_drived(self, distance):
		speed = float(distance)/self.time
		print '%s老妈骑着%s去买菜，平均速度为%skm/h' % (self.date,self.name,speed)
def main():
	car1 = Car('周一',0.5,'电动车')
	car1.be_drived(20)
	car2 = Car('周二',2,'自行车')
	car2.be_drived(20)
	car3 = Car('周三',0.6,'电动车')
	car3.be_drived(20)
if __name__ == '__main__':
	main()