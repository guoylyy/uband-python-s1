#!usr/bin/python
#coding:utf-8

import turtle,time

def main():
	win=turtle.Screen()
	win.bgpic("111.gif")
	win.bgcolor('orange')
	win.title("我的一个小铁锹……")

	mm = turtle.Turtle()
	mm.shape("circle")
	mm.shapesize(1,1,0)
	mm.setposition(150,-40)
	mm.clear()
	mm.color("red")
	mm.fillcolor("green")
	mm.speed(10)
	mm.pensize(2)

	mm.rt(90)	
	mm.fd(150)
	
	for x in xrange(1,100):		
		mm.setposition(150,-40)		
		mm.rt(x)
		mm.fd(150)

	mm.lt(90)
	mm.circle(150)

	time.sleep(20)

if __name__ == '__main__':
	main()
