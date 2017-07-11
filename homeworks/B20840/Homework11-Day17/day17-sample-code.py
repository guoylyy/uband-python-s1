#!/usr/bin/python
#_*_ coding:utf-8 _*_
#@author:B20840

import turtle

def main():
	#设置一个画面
	windows= turtle.Screen()
	#设置背景
	windows.bgcolor('red')
	#生成一个黄色乌龟
	bran = turtle.Turtle()


	#============
	arya = bran.clone() #克隆一只黑色的叫arya的乌龟
	#============

	
	bran.shape('turtle')
	bran.color('yellow')
	arya.shape('turtle')
	arya.color('black')


	#============
	#重新设置小乌龟arya的坐标
	arya.setx(10)
	arya.sety(240)
	#============


	#设置速度
	bran.speed(1)
	bran.circle(39,720)

	#走几步
	
	for i in range(1,10):
		
		arya.forward(100)
		arya.right(90)
		arya.forward(150)
		arya.right(90)
		arya.forward(100)
		arya.right(90)
		arya.forward(150)
		arya.right(90)
	#停下来

if __name__ == '__main__':
	main()