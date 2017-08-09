#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tangxiaocu

import turtle

def main():
	#设置一个画面
	windows = turtle.Screen()
	#设置背景
	windows.bgcolor('black')
	#生成一个黄色乌龟
	bran = turtle.Turtle()
	turtle.title("Welcome to the turtle zoo!")
	bran.shape('turtle')
	bran.color('yellow')
	
	#设置速度
	bran.write("biubiubiu = ", True, align="center")
    
	bran.speed(1)
	bran.circle(50,360,500)
	
	bran.pensize(10)
	bran.circle(100,360,500)
	bran.circle(20,360,500)
	
	#走几步
	# for i in range(1,30):
	# 	bran.forward(10)
	# 	bran.left(9)
	# 	bran.forward(10)
	# 	bran.left(9)
	# 	bran.forward(10)
	# 	bran.left(9)
	# 	bran.forward(10)
	# 	bran.left(9)
	# ctrl+/
	#停下来



if __name__ == '__main__':
	main()