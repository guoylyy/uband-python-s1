#!/usr/bin/python
#	-*-	coding:	utf-8	-*-
#	@author:	xxx
import	turtle

def main():
	#设置一个画面
	windows = turtle.Screen()
	#设置背景
	windows.bgcolor('red')
	#生成一个黄色乌龟
	bran	=	turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')
	bran.speed(1)
	ken	=	turtle.Turtle()
	ken.shape('turtle')
	ken.color('green')
	ken.speed(1)
	
	bran.goto(0,100)
	bran.circle(50,360,100)
	bran.home()
	
	bran.goto(125,0)
	bran.circle(50,360,100)
	bran.home()
	
	bran.goto(-125,0)
	bran.circle(50,360,100)
	bran.home()
	bran.goto(0,-150)
	bran.circle(175,360,100)

	bran.fd(200)
	bran.left(45)
	bran.fd(40)
	bran.left(45)
	bran.fd(50)
	bran.circle(50,360,100)
	bran.home()

	ken.goto(0,-200)
	ken.fd(100)
	ken.right(90)
	ken.fd(50)
	ken.right(90)
	ken.fd(200)
	ken.right(90)
	ken.fd(50)
	ken.right(100)
	ken.circle(50,360,100)
	ken.home()
	#走几步
	#for i in range(1,10):
	#	bran.forward(100)
	#	bran.right(90)
	#	bran.forward(150)
	#	bran.right(90)
	#	bran.forward(100)
	#	bran.right(90)
	#	bran.forward(150)
	#	bran.left(90)

	#	bran.forward(100)
	#	bran.left(90)
	#	bran.forward(150)
	#	bran.left(90)
	#	bran.forward(100)
	#	bran.left(90)
	#	bran.forward(150)
	#	bran.right(90)
	#停下来



if __name__ == '__main__':
	main()