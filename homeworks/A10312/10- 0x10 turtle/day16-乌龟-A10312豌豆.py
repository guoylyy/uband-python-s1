#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: wandou

import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('red')
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')

	bran.speed(1)

	bran.forward(120)
	bran.right(70)
	bran.forward(130)
	bran.right(80)
	bran.forward(150)
	bran.right (110)
	bran.forward(120)
	bran.right(70)




if __name__ == '__main__':
  main()