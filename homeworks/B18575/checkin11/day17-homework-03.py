#!/bin/usr/python
#-*- coding:utf-8 -*-
#@author:SKY
#打乌龟v1.0版本

import turtle
import random
import time
gd=[]
b=turtle.Turtle()
b.hideturtle()
b.up()
b.color("red")
b.shapesize(3,3)
b.goto(200,100)
def hit(i):
	b.clear()
	b.write(i)
def turn(x,y):
	global gd
	gd.append("1")
	hit(len(gd))
	

def runTurtle():
	windows=turtle.Screen()
	windows.bgcolor("blue")
	tu=[]
	i=0
	hit(i)
	for i in range(10):
		bran=turtle.Turtle()
		bran.hideturtle()
		bran.color("yellow")
		bran.shape("turtle")
		bran.shapesize(1,1)
		bran.onclick(turn)
		bran.up()
		bran.goto(i*30,0)
		tu.append(bran)
	while 1:
		n=(int)(random.uniform(0, 10))
		for i in range(10):
			tu[i].hideturtle()
		tu[n].showturtle()
		time.sleep(1)

def main():
	runTurtle()

if __name__ == '__main__':
	main()
