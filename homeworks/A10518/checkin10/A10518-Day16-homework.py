#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: fanyujie
import turtle
import time

def main():
	windows = turtle.Screen()
	windows.bgcolor('pink')
	allen = turtle.Turtle()
	allen.shape ('turtle') 
	allen.color('white')
	allen.speed(1)
	allen.pensize(5)
	allen.goto(0,0)
	for i in range(1):
		allen.forward(100)
		allen.right(90)
		allen.up()
		allen.goto(50,100)
		allen.down()
		allen.forward(200)
	time.sleep(3)


if __name__ == '__main__':
	main()