#!/usr/bin/python
# -*- coding: utf-8 -*
# @author: IPLAY
class Car():
	def __init__(self, brand,speed): #类的构造函数或初始化方法 #self 代表类的实例，self 在定义类的方法时是必须有的
		self.brand = brand
		self.speed = speed
	def be_driven(self, distance):
		hour = float(distance)/self.speed
		print "驾驶 %s 开 %d km 去b地开了 %0.2f 小时" %(self.brand, distance, hour) 
def main():
	car1 = Car('捷达',60)  #创建实例对象
	car1.be_driven(300) #访问属性


	car2 =Car('捷豹',120)
	car2.be_driven(400)
	
if __name__ == '__main__':
	main()