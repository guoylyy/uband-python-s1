#!/usr/bin/python
# -*- coding: utf-8 -*-

import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('blue')
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('black')
	bran.speed(1)

	bran.right(72)
	bran.forward(100)
	bran.right(144)
	bran.forward(100)
	bran.right(144)
	bran.forward(100)
	bran.right(144)
	bran.forward(100)
	bran.right(144)
	bran.forward(100)

if __name__ =='__main__':
	main()