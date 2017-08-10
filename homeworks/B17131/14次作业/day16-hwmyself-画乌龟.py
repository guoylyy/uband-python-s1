#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: youngmpjlt

import turtle #引入库

def main():
	#设置一个画面
	windows = turtle.Screen()
	#设置背景
	windows.bgcolor('purple')
	#生成一个黄色乌龟
	bran  = turtle.Turtle()
	bran.shape('turtle')
	bran.color('white')
	#设置速度
	bran.speed(1)
	#bran.setpos(45,100)#让乌龟直接到某个地方 

	#走几步
for i in range(1,100):#让它走十次
	bran.forward(144)#往前走100步
	bran.right(2)#往右转90度
	bran.forward(144)
	bran.right(5)
	bran.forward(144)
	bran.right(10)
	bran.forward(144)
	bran.right(15)  
	bran.forward(144)
	bran.right(18)
	bran.forward(144)
	bran.right(25)
	# ctrl + / 注释的快捷键
	

	   
	#停下来，让它走成一个正方形



if __name__ == '__main__':
	main()











