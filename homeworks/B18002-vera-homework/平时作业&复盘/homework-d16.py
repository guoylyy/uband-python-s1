#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: vera

import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('white')
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('red')
	bran.speed(1)

	for i in range(1,20):
		bran.forward(15) 
		bran.right(10)  
		bran.forward(15)
		bran.right(10)
		bran.forward(15)
		bran.right(10)
		bran.forward(15)
		bran.right(10)

if __name__ == '__main__':
	main()