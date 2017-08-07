#!/usr/bin/python
#-*- coding: utf-8 -*-
#@author:xxx

import turtle

def main():
	#设置一个画面
	windows=turtle.Screen()
	#设置背景
	windows.bgcolor('pink')
	#生成黄色的乌龟
	bran=turtle.Turtle()#后面的T一定要大写
	bran.shape('turtle')
	bran.color('purple')
	#设置速度
	bran.speed(1)

	for i in range(1,20):
		bran.forward(100)
		bran.left(72)
		bran.forward(100)
		bran.right(144)

if __name__ == '__main__':
	main()
