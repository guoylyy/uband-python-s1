#!/usr/bin/python
# -*- coding: utf-8 -*-
# 什么是面向对象
#我对面向对象的理解是对具体的事物进行定义和封装，是其抽象成现实世界的蓝图，然后这张蓝图可以在程序中反复生产出实例，可以重复使用。
#需求
# - 老妈的交通工具有两个，电动车和自行车
# - 家里离菜场共 20 公里
# - 周一的时候骑电动车去买菜，骑了 0.5 小时
# - 周二的时候骑自行车去卖菜，骑了 2 小时
# - 周三的时候骑电动车去卖菜，骑了 0.6 小时
# - 分别输出三天骑行的平均速度
class Bicycle():
	def __init__(self, day,name):
		self.name=	name
		self.day=	day

	def buy(self,distance,hour):
		speed	=	float(distance)/hour
		print	'%s骑%s平均时速%dkm/h	'	%(self.day,self.name,speed)

	def songs(self,times):
		print	'%s总共唱了%d首歌'	%(self.name,times)


			
def main():
	day1	=	Bicycle('周一	','电动车')
	day1.buy(20,0.5)		
	print	'------'
	day2	=	Bicycle('周二','自行车')
	day2.buy(20,2)
	print	'------'
	day3	=	Bicycle('周三','电动车')
	day3.buy(20,0.6)

#def main():
#  distance = 20

 # e_bicycle = '电动车'
  #bicycle = '自行车'

  #day1 = '周一'
#  hour1 = 0.5
#  speed1 = 20/hour1
#  print '%s 骑 %s 平均时速 %0.2f km/h' %(day1,e_bicycle, speed1)

#  day2 = '周二'
#  hour2 = 2
#  speed2 = 20/hour2
#  print '%s 骑 %s 平均时速 %0.2f km/h' %(day2,bicycle,speed2)

#  day3 = '周三'
#  hour3 = 0.6
#  speed3 = 20/hour3
#  print '%s 骑 %s 平均时速 %0.2f km/h' %(day3, e_bicycle, speed3)

if __name__ == '__main__':
  main()
