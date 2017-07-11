#! usr/bin/python
# -*- coding: utf-8 -*-
# @author:Emma

import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('black')

	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('pink')
	bran.speed(1)
	
	bran.circle(90,1000)

	bran.fillcolor('red')

	bran.hideturtle()
	
	for i in range(1,3):
	 	bran.stamp()
	 	bran.fd(300)


if __name__ == '__main__':
	main()