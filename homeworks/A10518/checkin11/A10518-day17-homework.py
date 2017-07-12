#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import turtle

def main():

  windows = turtle.Screen()
 
  windows.bgcolor('pink')
  turtle.shape('square')
  turtle.shapesize(stretch_wid=2, stretch_len=4, outline=6)
  
 
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('yellow', 'red')
  bran.speed(1)
  for i in range(1,20):
	bran.forward(10)
	bran.left(20)
	bran.forward(20)

  turtle.reset()
  turtle.shape("circle")
  turtle.shapesize(2,2)
  turtle.tilt(30)
  turtle.fd(50)
  turtle.tilt(90)
  turtle.fd(50)
  turtle.mainloop()
  def turn(x, y):
    left(180)
    onclick(turn)  # Now clicking into the turtle w>>> def turn(x, y):
  


if __name__ == '__main__': 
  main()