#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY
import turtle
import os
def main():
	#设置一个画面
	windows = turtle.Screen()
	#设置背景
	windows.bgcolor('blue') #默认白色的背景
	#生成一个黄色的乌龟
	bran1 = turtle.Turtle()
	bran1.shape('turtle')  #默认黑色的乌龟
	bran1.color('yellow')

	bran2 = turtle.Turtle()
	bran2.shape('turtle')  
	bran2.color('red')
	bran3 = turtle.Turtle()
	bran3.shape('turtle')  
	bran3.color('green')
	bran4 = turtle.Turtle()
	bran4.shape('turtle')  
	bran4.color('pink')
	bran5 = turtle.Turtle()
	bran5.shape('turtle')  
	bran5.color('orange')
	#设置速度
	# bran.speed(1)
	# bran.circle(120,720) #720意味着两圈
	bran1.position()
	(0.00,0.00)
	bran1.forward(100)
	bran1.position()
	(100.00,00.00)
	bran1.forward(-75)
	bran1.position()
	(-50.00,0.00)
	bran1.circle(50,360)
	bran1.clear()
	

	bran2.position()
	(100.00,100.00)
	bran2.backward(30)
	bran2.position()
	(20.0,100.00)
	bran2.circle(50,360)
	bran2.clear()

	bran3.hideturtle()
	bran3.backward(100)
	bran3.showturtle()
	bran3.circle(50,360)
	bran3.clear()

	bran4.write("Home =", True, align = 'center')
	bran4.write((0,0), True)
	bran4.left(100)
	bran4.circle(50,360)
	bran4.color('purple')
	bran4.write('Done')
	bran4.clear()

	bran5.pensize(5)
	bran5.goto(0,0)
	bran5.speed(10)
	for i in range(6):
		bran5.forward(100)
		bran5.right(144)
	bran5.up
	bran5.forward(100)
	bran5.goto(-150,-120)
	bran5.write('Done')

	os.system("pause")
if __name__ == '__main__':
	main()