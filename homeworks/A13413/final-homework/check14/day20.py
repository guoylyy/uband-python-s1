#!/usr/bin/python
# -*- coding: utf-8 -*-

class Bicycle():
	def __init__(self, day, kind, hour):
		self.day = day
		self.kind = kind
		self.hour = hour

	def be_drived(self, distance):
		speed = float(distance)/self.hour
		print '%s 老妈骑 %s 去菜市场买菜平均时速 %0.2f km/h' %(self.day, self.kind, speed)

def main():
	bicycle1 = Bicycle('周一', 'e_bicycle', 0.5)
	bicycle1.be_drived(20)

	bicycle2 = Bicycle('周二' 'bicycle', 2)
	# bicycle2.be_drived(20)

	bicycle3 = Bicycle('周三' 'e_bicycle', 0.6)
	bicycle3.be_drived(20)



if __name__ == '__main__':
	main()



		