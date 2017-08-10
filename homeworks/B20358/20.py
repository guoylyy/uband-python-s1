#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Anna

class Traffic():
	def __init__(self, tool, date, hour):
		self.tool = tool
		self.date = date
		self.hour = hour

	def be_drived(self, distance):
		speed = float(distance)/self.hour
		print '%s 老妈驾驶 %s 开 %skm 去买菜, 骑了 %s小时, 平均时速 %0.2f km/h' % (self.date, self.tool, distance, self.hour, speed)

def main():
	traffic1 = Traffic('电动车', '周一', 0.5)
	traffic1.be_drived(20)

	traffic2 = Traffic('自行车', '周二', 2)
	traffic2.be_drived(20)

	traffic3 = Traffic('电动车', '周三', 0.6)
	traffic3.be_drived(20)


if __name__ == '__main__':
	main()