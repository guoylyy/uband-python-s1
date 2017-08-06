#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: pluto

import turtle

def main():
  windows = turtle.Screen()
  windows.bgcolor('white')
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('red')
  bran.speed('slowest')
  bran.left(45)
  bran.fd(50)

  joe = bran.clone()
  joe.color('blue')
  joe.circle(50,180)

  bran.left(90)
  bran.fd(100)
  joe.rt(90)
  joe.fd(100)
  bran.rt(90)
  bran.circle(50,90)
  joe.circle(50,180)

  joe.tilt(30)
  joe.fd(50)
  joe.tilt(30)
  joe.fd(50)

  joe.home()

  bran.dot()

if __name__ == '__main__':
  main()