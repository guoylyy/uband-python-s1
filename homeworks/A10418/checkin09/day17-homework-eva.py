#!/usr/bin/python
# -*- coding: utf-8 -*-

#注释的快捷键：command+/

import turtle

def main1():
	#设置一个画面
	windows = turtle.Screen()

	#设置背景
	windows.bgcolor('pink')

	#生成一个白色乌龟
	bran = turtle.Turtle()
	happy=bran.clone()
	bran.shape('turtle')
	bran.color('white')
	bran.pensize(10)

	#设置速度
	bran.speed(1)
	bran.circle(100,360,30)
	turtle.delay(50)


	#走几步
	# for i in range(1,10):
	# 	bran.forward(100)
	# 	bran.right(90)
	# 	bran.forward(100)
	# 	bran.right(90)
	# 	bran.forward(100)
	# 	bran.right(90)
	# 	bran.forward(100)
	# 	bran.right(90)

if __name__ == '__main__':
	main1()


