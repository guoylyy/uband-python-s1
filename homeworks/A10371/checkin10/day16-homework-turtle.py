#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yuanzi
import turtle

def main():
	#设置一个画面
	windows = turtle.Screen()
	#设置背景
	windows.bgcolor('pink')
	#生成一个绿色的乌龟
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('green')
	#设置速度
	bran.speed(1)
	#走几步
	for i in range(1,10):
		
		bran.forward(40)
		bran.left(45)
		bran.backward(50)
		bran.left(90)
		bran.forward(50)
		bran.right(135)
		bran.forward(40)
	#停下来

if __name__ == '__main__':
	main()