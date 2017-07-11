#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: lightningLUO
#画乌龟

import turtle

def main():
	#设置一个画面
	windows = turtle.Screen()
	#
	windows.bgcolor('blue')
	jack = turtle.Turtle()
	jack.shape('turtle')
	jack.color('green')
	jack.speed(1)

	for i in range (1,10):
		jack.forward(100)
		jack.right(120)
		jack.forward(100)
		jack.right(120)
		jack.forward(100)

if __name__ == '__main__':
	main()
