#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import turtle

def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('blue')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('yellow')
  turtle.hideturtle()
  #开始你的表演
  for i in range(1,6):
    bran.speed(5)
    bran.right(72)
    bran.forward(100)
    bran.right(144)
    bran.forward(100)
    bran.right(144)
    bran.forward(100)
    bran.right(144)
    bran.forward(100)
    bran.right(144)
    bran.forward(100)
  bran.circle(120, 360)
  bran.circle(100, 360)
  bran.circle(80, 360)
  bran.circle(60, 360)

 
if __name__ == '__main__':
  main()