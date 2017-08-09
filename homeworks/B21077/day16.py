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
	windows.bgcolor('green')
	#生成一个黄色乌龟
	bran=turtle.Turtle()
	bran.shape('turtle')
	bran.color('red')
	#设置速度
	bran.speed(1)
	for i in range(1,5):#把for语句 放在def main底下有什么不同？为什么？（循环的部分不一样！！！）
	#走几步
		bran.forward(400)
		bran.right(144)
		bran.forward(400)
		bran.right(144)
		bran.forward(400)
		bran.right(144)
		bran.forward(400)
		bran.right(144)
	#停下来

if __name__ == '__main__':
	main()