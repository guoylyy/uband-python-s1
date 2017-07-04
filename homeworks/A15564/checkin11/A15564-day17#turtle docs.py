#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: shangxindepidan

import turtle

import math
length = 200  
degrees_18 = math.radians(18)  # convert 18° to corresponding radians
cos18 = math.cos(degrees_18) # cos(18°)
sin18 = math.sin(degrees_18) # sin(18°)
radius = length/2/cos18

def main():
  #set a window
  window = turtle.Screen()
  #set bg
  window.bgcolor('red')


  #turtle white
  bran2 = turtle.Turtle()
  bran2.shape('turtle')
  bran2.color('white')
  bran2.setheading(180) # mirror
  #motion
  turtle_graphic(bran2)

  #turtle black
  bran1 = turtle.Turtle()
  bran1.shape('turtle')
  bran1.color('black')
  #motion
  turtle_graphic(bran1)

  ##circles
  circles_white(radius, cos18, sin18, bran2)
  circles_black(radius, cos18, sin18, bran1)

  for i in range(1,10086):  # spin * 2 * 10086
    bran1.rt(360)
    bran2.lt(360)
  
def circles_black(radius, cos18, sin18, bran1):
  n = 1
  while n < 4:
    x = radius * cos18 * n/4
    y = -(radius * sin18 * n/4)
    bran1.penup()
    bran1.setposition(x,y)
    bran1.pendown()
    bran1.circle(radius*(4-n)/4,360)
    n = n + 1
  bran1.penup()
  bran1.setposition(x*n/(n-1),y*n/(n-1))
  bran1.dot(radius/n*2,'white')

def circles_white(radius, cos18, sin18, bran2):
  n = 1
  while n < 4:
    x = -radius * cos18 * n/4
    y = (radius * sin18 * n/4)
    bran2.penup()
    bran2.setposition(x,y)
    bran2.pendown()
    bran2.circle(radius*(4-n)/4,360)
    n = n + 1
  bran2.penup()
  bran2.setposition(x*n/(n-1),y*n/(n-1))
  bran2.dot(radius/n*2,'black')

def turtle_graphic(turtle):
  turtle.speed(1)
  turtle.width(3) # set pentagram width
  for i in range(1,6): # pentagram
    turtle.forward(length)
    turtle.right(144)  # now heading 0.0
  turtle.right(108) # or bran.setheading(252) #adjust heading to 252.0
  turtle.width(5) # set outer circle width
  turtle.circle(radius,360) # circle around pentagram
  turtle.width(1) # set inner circles width
  

if __name__ == '__main__':
  # main()
  pass


def t_write(turtle, radius):
  turtle.penup()
  turtle.color('black')
  turtle.goto(0,4.5*radius)
  turtle.pendown()
  turtle.write("Captain A", font=("Helvetica", 58, "bold"))

  turtle.penup()
  turtle.color('black')
  turtle.goto(5*radius,3.5*radius)
  turtle.pendown()
  turtle.write("@sxdpd", font=("Helvetica", 18, "italic"))

def captain_A():
  length = 100
  radius = length/2/cos18

  window = turtle.Screen()
  window.bgcolor('white')
  t = turtle.Turtle()
  t.shape('classic')
  
  t.penup()  
  t.setposition(0,-4*radius)
  t.pendown()
  t.begin_fill()
  t.fillcolor('#86323C') # red
  t.circle(4*radius)
  t.end_fill()

  t.penup()  
  t.setposition(0,-3*radius)
  t.pendown()
  t.begin_fill()
  t.fillcolor('#F3F3F3') # white
  t.circle(3*radius)
  t.end_fill()

  t.penup()  
  t.setposition(0,-2*radius)
  t.pendown()
  t.begin_fill()
  t.fillcolor('#86323C') # red
  t.circle(2*radius)
  t.end_fill()

  t.penup()  
  t.setposition(0,-1*radius)
  t.pendown()
  t.begin_fill()
  t.fillcolor('#1C2B45') # blue
  t.circle(1*radius)
  t.end_fill()

  side = length / (2 * (1 + sin18)) # [(length/2) - side] / side = sin18°
  # print side, length, sin18

  t.penup()  
  t.setposition(0,1*radius) # now heading 0.0
  t.pendown()
  t.right(72)

  t.begin_fill()
  t.fillcolor('#F0F6F8') # white
  for i in range(1, 6):
    t.fd(side)
    t.lt(72)
    t.fd(side)
    t.rt(144)
  t.end_fill() # now heading 288.0


  t_write(t, radius)

  for i in range(1,10086):
    t.rt(360)



if __name__ == '__main__':
  captain_A()