#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:Muzi

import turtle
def main():
	
	windows=turtle.Screen()
	windows.bgcolor('red')
	bran=turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')
	bran.speed(5)
	for x in xrange(1,6):
		bran.forward(400)
		bran.right(144)
		bran.forward(400)
		bran.right(144)
		bran.forward(400)
		bran.right(144)
		bran.forward(400)
		bran.right(144)
		
		
		

		
if __name__ == '__main__':
	main()


