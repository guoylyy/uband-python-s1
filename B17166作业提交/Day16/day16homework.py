#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('red')
	bran=turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')


	bran.speed(2)

	for i in range(1,10):
		bran.forward(100)
		bran.right(50)
		bran.forward(100)
		bran.right(50)
		bran.forward(100)
		bran.right(50)
		bran.forward(100)
		bran.right(50)
if __name__ == '__main__':
	main()
