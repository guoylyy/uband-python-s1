#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B20769-feiyu

import turtle  #引入turtle这个库

def main():
	windows = turtle.Screen()  #建立一个Windows窗口
	windows.bgcolor('black')   #窗口背景颜色为black
	bran = turtle.Turtle()     #窗口中设置一个图形
	bran.shape('turtle')       #设置图形为乌龟
	bran.color('yellow')       #设置乌龟的颜色为yellow
	bran.speed(1)              #乌龟运动的速度为1
	for i in range(1,300):     #建立一个循环
		bran.forward(100)      #乌龟向前运动100步，每一步运动1个单位
		bran.right(90)         #乌龟右转90°
		bran.backward(100)     #乌龟向后运动100步，每一步运动1个单位
		bran.left(90)          #乌龟右转90°

if __name__ == '__main__':
  main()