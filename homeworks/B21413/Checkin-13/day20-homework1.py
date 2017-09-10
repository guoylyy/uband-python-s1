#!/usr/bin/python
# -*- coding: utf-8 -*-

class Vehicle():
	def __init__(self,day,specis,hour):
		self.day = day
		self.specis = specis
		self.hour = hour

	def be_drived(self,distance):
		speed = float(distance) / self.hour
		print '%s 骑 %s 平均时速 %0.2f km/h' %(self.day,self.specis,speed)

		#在这段面向对象的代码之中，vehicle作为一个类。其基本属性，还有基于属性的行为被定义了之后。
		#在下方具体到产生变量的执行代码条之中，执行的就是class这个大类（系统）下的变化。
		#与一般之前的用函数来定义行为不同的在于，类作为‘蓝图’，类具有更多大的包容性和复杂度。

def main():
	day1 = Vehicle('周一','电动车',0.5)
	day1.be_drived(20)

	day2 = Vehicle('周二','自行车',2)
	day2.be_drived(20)

	day3 = Vehicle('周三','电动车',0.6)
	day3.be_drived(20)


if __name__ == '__main__':
  main()
