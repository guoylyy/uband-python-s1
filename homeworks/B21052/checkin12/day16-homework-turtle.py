#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: caramel
import turtle

def main():
	#设置一个画面
	windows = turtle.Screen()
	#设置背景
	windows.bgcolor('pink')
	#生成一个黄色的乌龟
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('purple')
	#设置速度
	bran.speed(1)
	#走几步
	for i in range(1,10):  #乌龟走10次
		bran.forward(100)  #前进100
		bran.left(72)     #右拐90度
	 	bran.forward(100)  #前进150
	 	bran.right(144)     #右拐90度
	 	
	#停下来


if __name__ == '__main__':
  main()