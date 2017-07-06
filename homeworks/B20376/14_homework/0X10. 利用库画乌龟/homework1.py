#! usr/bin/python
# -*- coding: utf-8 -*-
# @author:Emma

import turtle

def main():
	#设置一个画面
	windows = turtle.Screen()
	#设置背景
	windows.bgcolor('black')
	#生成一个黄色乌龟
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('red')
	#设置速度
	bran.speed(1)
	#走几步
	for i in range(1,10):
		bran.forward(100)
		bran.left(90)
		bran.forward(150)
		bran.right(90)
		bran.forward(100)
		bran.right(90)
		bran.forward(150)
		bran.right(90)


if __name__ == '__main__':
	main()