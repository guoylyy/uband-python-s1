#!/usr/bin/python
#	-*-	coding:	utf-8	-*-
#	@author:	xxx


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


if __name__ == '__main__':
	main()