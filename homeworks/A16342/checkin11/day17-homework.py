#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yan

import turtle

def main():
	windows = turtle.Screen()
	windows.bgcolor('pink')

	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')

	bran.speed(1)
	#write 打字
	bran.write('hello')
	bran.forward(200)
	
	#penup移动的时候不划线
	#goto移动到某个坐标
	bran.penup()
	bran.goto(50,50)
	#dot画点
	bran.dot(10,'red')
	bran.goto(100,100)
	
	#down,penup对应语句，放下笔
	bran.down()
	bran.forward(200)



if __name__ == '__main__':
	main()