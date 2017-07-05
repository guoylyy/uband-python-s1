#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Winnie

import turtle
def main():
	windows = turtle.Screen()
	windows.bgcolor('white')
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow','red')
	bran.speed(1)
	bran.circle(100,100,100)

def main2():
	windows = turtle.Screen()
	windows.bgcolor('white')
	ben = turtle.Turtle()
	ben.shape("turtle")
	ben.color('blue','black')
	ben.speed(1)
	for i in range(1,20):
		ben.circle(100,100,200)
	
	

	# for i in range(1,10):
	# 	bran.forward(100)
	# 	bran.right(90)
	# 	bran.forward(150)
	# 	bran.right(90)
	# 	bran.forward(100)
	# 	bran.right(90)
	# 	bran.forward(100)
	# 	bran.right(90)
	# 	bran.forward(150)
	# 	bran.right(90)
	# 	bran.forward(100)
	# 	bran.right(90)

	

if __name__ == '__main__':
  main()
  main2()



