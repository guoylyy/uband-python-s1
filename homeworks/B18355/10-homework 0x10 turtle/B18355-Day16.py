#!/usr/bin/python
#-*- coding:utf-8 -*-
# Filename:B18355-Day16.py
# @author:清蒸

import turtle

def main():
	#设置一个画面
	windows = turtle.Screen()
	#设置背景
	windows.bgcolor('yellow')
	#生成一个乌龟---绿色
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('green')
	#设置速度-----0.1很快，10也很快...是不是1是最小速度了？？
	bran.speed(2)
	#走几步？
	for i in range(1,3):
		bran.forward(100)
		bran.right(90)
		bran.forward(120)
		bran.right(90)
		bran.forward(100)
		bran.right(90)
		bran.forward(120)
		bran.right(90)

if __name__ == '__main__':
	main()