#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xb
import turtle

def main():

  windows = turtle.Screen()

  windows.bgcolor('black')

  bran = turtle.Turtle()
  qwe = turtle.Turtle()
  bran.shape('turtle')
  bran.color('yellow')
  qwe.shape('turtle')
  qwe.color('red')

  bran.circle(50,180,40)
  qwe.circle(50,-180,40)
  bran.left(45)
  qwe.right(45)
  bran.right(45)
  qwe.left(45)
  for i in range(1,2):
    bran.back(50)
    bran.left(90)
    bran.forward(100)
    bran.right(90)
    bran.forward(100)
    bran.right(90)
    bran.forward(100)
    bran.right(90)
    bran.forward(50)
    
    qwe.back(50)
    qwe.left(-90)
    qwe.forward(100)
    qwe.right(90)
    qwe.forward(-100)
    qwe.right(90)
    qwe.forward(100)
    qwe.left(90)
    qwe.forward(50)


   

if __name__ == '__main__':
  main()