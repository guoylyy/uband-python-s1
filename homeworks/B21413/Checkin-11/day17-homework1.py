#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 190
import turtle

def main():
	#设置画面
	windows = turtle.Screen()
	#设置背景
	windows.bgcolor('blue')
	#生成小乌龟
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('white')
	
	#设置速度
	bran.speed(2)
	#走四方
	for i in range(1,12):
		bran.forward(25)
		bran.right(90)
		bran.forward(30)
		bran.left(90)
		bran.forward(25)
		bran.right(90)
		bran.forward(30)
		bran.right(90)
	



if __name__ == '__main__':
  main()