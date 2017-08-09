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
  #开始你的表演
  bran.speed(30)
  for i in range(1,9):
    tp = turtle.pos()
    tp
    (0.00,0.00)
    turtle.setpos(100,160)
    turtle.pos()
    (90.00,160.00)
    turtle.setpos((100,160))
    turtle.pos()
    (120.00,280.00)
    turtle.setpos(tp)
    turtle.pos()
    (0.00,0.00)

if __name__ == '__main__':
  main()