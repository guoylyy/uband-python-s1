#!/usr/bin/python
#coding:utf-8
import turtle,time

def main():
	windows = turtle.Screen()
	windows.bgcolor('red')
	bran = turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')
	bran.speed(1)

	time.sleep(5)

	for x in xrange(1,10):
		bran.forward(100+x)
		bran.right(90)
		bran.forward(150+x)
		bran.right(90)
		bran.forward(100+x)
		bran.right(90)
		bran.forward(150+x)


if __name__ == '__main__':
	main()