#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('blue')
	bran = turtle.Turtle()
	bran.shape('classic')
	bran.color('yellow','blue')
	bran.shapesize(1,1)
	bran.speed(3)

	for i in range(1,6):
		bran.fd(100)
		bran.lt(72)
		bran.fd(100)
		bran.rt(144)

	bran.back(200)
	bran.setposition(-200,-100)
	bran.shape('turtle')
	bran.stamp()
	bran.circle(100,360)






		

	

	# bran.back(200)

	# bran.lt(20)




	# bran.forward(200)

	# bran.setposition(-100,-100)
	# bran.rt(45)
	# bran.fd(100)

	# bran.home()

	# bran.stamp()
	# bran.fd(100)

	# bran.clearstamps()

	# bran.circle(100,360)

	# bran.get_poly()


	#bran.goto(10, 10)
		#bran.setheading(80)







	# for i in range(1,2):
	# 	bran.forward(10)
	# 	bran.left(2)
	# 	bran.forward(10)
	# 	bran.right(2)
	# 	bran.forward(10)
	# 	bran.left(2)
	# 	bran.forward(10)
	# 	bran.left(2)





if __name__ == '__main__':
	main()