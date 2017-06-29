#!/usr/bin/python
# -*- coding: utf-8 -*-

import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('white')

	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('black')

	bran.speed(1)

	for i in range(1,10):

		bran.forward(100)
		bran.right(150)
		bran.forward(200)
		bran.right(90)
		bran.forward(100)
		bran.right(90)
		bran.forward(200)
		bran.right(90)


if __name__ == '__main__':
	main()