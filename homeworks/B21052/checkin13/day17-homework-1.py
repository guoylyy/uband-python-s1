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
	#设置速度
	bran.speed(1)
	bran.circle(90,360,3)   #90指半径，360指角度范围，3指步数，逆时针画一个三角形
	#bran.circle(90,720,3)   #90指半径，720指角度范围，3指步数，顺时针画一个三角形
	#bran.circle(90,360,6)   #90指半径，360指角度范围，6指步数，逆时针画一个六边形
	#bran.circle(90,720,6)   #90指半径，720指角度范围，6指步数，逆时针重复画一个三角形
	#bran.circle(90,360,9)    #90指半径，360指角度范围，9指步数，逆时针画一个九边形
	#bran.circle(90,720,100)    #90指半径，720指角度范围，10指步数，逆时针重复画一个五边形


if __name__ == '__main__':
  main()