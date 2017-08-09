#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: joylin

import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('red')
	# windows.setup (width=200, height=200, startx=0, starty=0)
	# windows.setup(width=.75, height=0.5, startx=None, starty=None)


	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')
	bran.speed(3)
	for i in range(1,10):
		bran. forward(90)
		bran. right(60)
		bran. forward(120)
		bran. right(60)
		bran. forward(90)
		bran. right(60)
		bran. forward(120)
		bran. right(90)

if __name__ == '__main__':
	main()

print turtle.position()

