#!/usr/bin/python
# -*- coding: utf-8 -*-

import turtle

def main():
	windows=turtle.Screen()
	windows.bgcolor('black')
	bran=turtle.Turtle()
	bran.shape('turtle')
	bran.color('white')
	bran.speed(1)
	for i in range(1,10):
		bran.forward(100)
		bran.left(90)
		bran.forward(100)
		bran.left(90)
		bran.forward(100)
		bran.left(90)
		bran.forward(100)
		bran.left(90)

if __name__ == '__main__':
  main()