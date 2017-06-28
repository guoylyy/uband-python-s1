#!/usr/bin/python

import turtle

def main():
	windows= turtle.Screen()
	windows.bgcolor('blue')
	bran=turtle.Turtle()
	bran.shape('turtle')
	bran.color('yellow')
	bran.speed(2)
	bran.forward(100)

	bran.backward(300)
	bran.heading()
	
	bran.left(60)
	bran.forward(200)
	bran.right(120)
	
	bran.forward(200)
	bran.setpos(60,100)
	bran.forward(120)
	bran.left(120)
	bran.forward(100)
	bran.right(120)
	bran.forward(100)
	bran.setx(200)
	bran.sety(-120)
	bran.right(120)
	bran.forward(400)
	bran.right(90)
	bran.forward(120)
	bran.fd(200)
	bran.rt(120)
	bran.forward(50)
	bran.rt(120)
	bran.forward(50)

if __name__ == '__main__':
	main()