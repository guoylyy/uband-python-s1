#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: lightningLUO
import turtle

def main():
 
  windows = turtle.Screen()

  windows.bgcolor('blue')
  Jack = turtle.Turtle()  

  Jack.shape('turtle')
  Jack.color('yellow')
  Jack.speed(1)
 
  Jack.dot()
  Jack.fd(100); Jack.dot(10,'white'); Jack.fd(50)
  
  Jack.circle(120,360,500)


if __name__ == '__main__':
  main()