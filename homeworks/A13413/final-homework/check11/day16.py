#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: joylin

import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('red')

	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')
	bran.speed(3)
	for i in range(1,8):
		bran.forward(90)
		bran.right(60)
		bran.forward(120)
		bran.right(60)
		bran.forward(90)
		bran.right(60)
		bran.forward(120)
		bran.right(60)



if __name__ == '__main__':
	main()