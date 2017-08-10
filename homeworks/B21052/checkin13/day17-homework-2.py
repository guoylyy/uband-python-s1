#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: caramel
import turtle

def main():
	#设置一个画面
	windows = turtle.Screen()
	#设置背景
	windows.bgcolor('red')
	#生成一个黄色乌龟
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')
	#开始你的表演
	#turtle motion
	# turtle.forward(200)    # = turtle.fd(100) 正方向移动100像素
	# #turtle.fd(-300)        #负方向移动300像素
	# #turtle.backward(400)     # bk 负方向移动400像素
	# turtle.right(90)         # = turtle.rt(90)顺时针旋转90度
	# turtle.fd(100)
	# turtle.lt(90)
	# turtle.bk(200)
	
	turtle.shape("circle")
	turtle.shapesize(1,5)
	turtle.tilt(90)   #顺时针翘起90度
	turtle.fd(200)
	

if __name__ == '__main__':
  main()