#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zi le

import turtle

def main():
	windows=turtle.Screen()
	windows.bgcolor('blue')
	bran=turtle.Turtle()
	bran.shape('turtle')
	bran.color('red')
	bran.speed(1)
	for i in range(1,10):
		bran.forward(150)
		bran.right(90)
		bran.forward(150)
		bran.right(60)
		bran.forward(100)

if __name__=='__main__':
	main()		


