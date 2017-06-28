#!/usr/bin/python
# -*- coding: utf-8 -*-

class Car():
	def __init__(self,name,brand):
		self.name=name
		self.brand=brand
		
	def be_drived(self,day,distance,hour):
		distance=20
		self.day=day
		speed= float(distance)/hour
		print '%s , %s 驾驶着 %s 去菜市场买菜，时速%0.2f小时' % (self.day,self.name,self.brand,speed)
def main():
	Car1 = Car( '老妈','电动车')
	Car1.be_drived('周一',20,0.5)
	Car2 = Car('老妈','自行车')
	Car2.be_drived('周二',20,2)
	Car3 = Car('老妈','电动车')
	Car3.be_drived('周三',20,0.6)

if __name__ == '__main__':
	main()




