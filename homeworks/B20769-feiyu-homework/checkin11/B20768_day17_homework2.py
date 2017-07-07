#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: feiyu
#输出turtle与下一点之间的距离，并直线去到下一点
import turtle 

def main():
	windows = turtle.Screen()
	windows.bgcolor('black')
	bran = turtle.Turtle()
	bran.setposition(-200,0)
	bran0 = turtle.Turtle()
	bran0.setposition(0,200)
	print '距离下一个乌龟的距离为：' 
	distance = bran.distance(0,200)
	print distance
	bran.shape('turtle')
	bran0.shape('turtle')
	bran.color('red')
	bran0.color('blue')
	bran.speed(1)
	bran.left(45)
	bran.forward(distance)
		

if __name__ == '__main__':
  main()
