#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: eros
 
import turtle
 
def main():
  windows = turtle.Screen()
  windows.bgcolor('blue')
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('red')
  bran.speed(5)

  for i in range(1,10):
     bran.forward(100)
     bran.right(90)
     bran.forward(100)
     bran.right(90)
     bran.forward(100)
     bran.right(90)
     bran.forward(100)
     bran.forward(100)
     bran.right(90)
     bran.forward(100)
     bran.right(90)
     bran.forward(100)
     bran.right(90)
     bran.forward(100)
  # turtle.circle(50,360,100)

if __name__ == '__main__':
	main()




