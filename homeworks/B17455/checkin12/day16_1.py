#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('blue')
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')
	bran.speed(1)

	for i in range(1,8):
		bran.forward(100)
		bran.left(90)
		bran.forward(150)
		bran.right(90)
		bran.forward(100)
		bran.left(45)
		bran.forward(150)
		bran.left(90)





if __name__ == '__main__':
	main()