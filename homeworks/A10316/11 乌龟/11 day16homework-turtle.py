#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: sanlianyin

import turtle

def main():
  windows = turtle.Screen()  #设置画面
  windows.bgcolor('blue')   #背景色


  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('yellow')

  bran.speed(1)


  for i in range(1,10):
  
    bran.forward(100)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
    bran.forward(100)
    bran.right(90)
    bran.forward(150)
    bran.right(90)


if __name__ == '__main__':
  main()