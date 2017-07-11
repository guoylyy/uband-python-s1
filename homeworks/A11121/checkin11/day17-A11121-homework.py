#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Jinxiao
'''
库的引用与文档的查找：
工具：
dash app MAC应用 
devdocs.io网站 WIN MAC都可
ctrl+/也可以注释掉
'''

import turtle
def main():
	windows = turtle.Screen()
	windows.bgcolor  ('green')
	windows.delay(20)
	ben = turtle.Turtle()
	ben.shape ('turtle')
	ben.color ('blue')
	ben.circle(50,720)
	ben.home()
	ben.begin_poly()
	ben.fd(100)
	ben.left(20)
	ben.fd(30)
	ben.left(60)
	ben.fd(50)
	ben.end_poly()

	jane = turtle.Turtle()
	jane.shape('turtle')
	jane.dot(20,'yellow')
	jane.color('red')
	jane.goto(-30,100)
	jane.circle(80,960)

	
	



if __name__ == '__main__':
	main()