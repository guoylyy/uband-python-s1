##!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

#python library:什么是库？？？利用程序员之前的工作，就是使用库（其他人写过的代码）去做其他的程序。
#应用外部的库画了一个乌龟
import turtle#引入外部的库

def main():
	#设置一个画面
	windows=turtle.Screen()
	#设置背景
	windows.bgcolor('pink')
	#生成一个黄色乌龟
	bran=turtle.Turtle()#Turtle是一个类！！！引入Turtle，调用turtle里面的类，实例化，形成一个叫BRAN的乌龟
	#一个类（蓝图）包含了描述它的东西。
	bran.shape('turtle')
	bran.color('black')
	bran.speed(1.00)
	bran.setpos(-100,130)#设置龟龟的坐标
	bran.home()#把乌龟带到起始坐标




	
	#joe = bran.clone()
	#joe.setpos(100.130)
	#bran.setx(100)#把bran改成turtle会怎样？？？试试？why???
	
	#turtle.pos()(60.00,30.00)
	#设置速度
	#bran.speed(1)
	#turtle.stamp ()
	
	#bran.circle(100,360,100)#半径，角度，线条数（因为是根据多边形来画圆的！这个数越大，乌龟越慢但越像圆）
	#走几步
	# for i in range(1,15):
	# 	bran.forward(10)
	# 	bran.right(20)
	# 	bran.forward(10)
	# 	bran.right(20)
	# 	bran.forward(10)
	# 	bran.right(20)
	# 	bran.forward(10)
	# 	bran.right(20)
	# #停下来

if __name__ == '__main__':
	main()