#!/usr/bin/python
# -*- coding: utf-8 -*-

import turtle
def collins():
	print '我叫RAY,我会爬哦'
	print '虽然我很笨，但我还是会爬=,='

def main():
	windows = turtle.Screen()
	windows.bgcolor('yellow')

	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('black')
	bran.speed(1)

	bran.circle(100,360,100)
    

	collins = bran.clone()
	collins.shapesize(6,6,6)
	for i in range(1,10):

		collins.forward(100)
		collins.right(150)
		collins.forward(200)
		collins.right(90)
		collins.forward(100)
		collins.right(90)
		collins.forward(200)
		collins.right(90)

	

if __name__ == '__main__':
	collins()
	main()
