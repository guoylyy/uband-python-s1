#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: vera

import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('white')
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('red')
	bran.fillcolor('purple')
	bran.width(2)
	bran.speed(3)
	brown = turtle.Turtle()
	brown.shape('turtle')
	brown.color('red')
	brown.fillcolor('purple')
	brown.width(2)
	brown.speed(3)
	# 画圆
	bran.circle(100,540,100)
	bran.setheading(90)
	bran.setheading(90)
	bran.circle(50,360,100)
	bran.setheading(180)
	bran.circle(50,360,100)
	bran.setheading(270)
	bran.circle(50,360,100)
	bran.setheading(360)
	bran.circle(50,360,100)
	# 画多边形
	# bran.home()
	# # bran.stamp()
	# bran.begin_poly()
	# bran.forward(300) 
	# bran.lt(120)
	# bran.forward(100)   
	# bran.lt(60)
	# bran.forward(200) 
	# bran.lt(60)
	# bran.forward(100)   
	# bran.get_poly()

	brown.begin_poly()
	brown.forward(300) 
	brown.lt(120)
	brown.forward(100)   
	brown.lt(60)
	brown.forward(200) 
	brown.lt(60)
	brown.forward(100)   
	brown.get_poly()


if __name__ == '__main__':
	main()