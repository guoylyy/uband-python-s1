#!/usr/bin/python
# -*- coding:utf-8 -*-

class Time():
	def __init__(self,day,hour):
		self.day=day
		self.hour=hour
	def drive(self,tool):
		distance=20
		speed=float(distance)/self.hour
		print '老妈周%s,骑%s去买菜,平均速度是:%0.2fkm/h'%(self.day,tool,speed)
def main():
	time1=Time('一',0.5)
	time1.drive('电动车')
	time2=Time('二',2)
	time2.drive('自行车')
	time3=Time('三',0.6)
	time3.drive('电动车')
if __name__ == '__main__':
	main()