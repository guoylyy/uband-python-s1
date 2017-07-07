#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: feiyu
#给乌龟定位并输出乌龟所在的位置 
import turtle 

def main():
	windows = turtle.Screen()
	windows.bgcolor('black')
	color = ['red','yellow','blue','green']
	bran = [1,2,3,4]
	for n in range(0,4):
		bran[n] = turtle.Turtle()
		x = -250+(n+1)*100
		y = 0
		bran[n].setposition(x,y)
		bran[n].shape('turtle')
		bran[n].color(color[n])
		bran[n].speed(1)
		bran[n].circle(75)
		print '第 %d 个乌龟的位置为：' % (n+1)
		print bran[n].position()
		

if __name__ == '__main__':
  main()