#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import turtle

def click(bran):
  bran.color('red')
  bran.speed(1)
  bran.circle(120, 720)


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
  # bran.circle(50,360,1000)
  
  bran.onclick(click(bran))

  for i in range(4):
    bran.speed(1)
    bran.fd(50)
    bran.lt(80)

  for i in range(8):
    turtle.undo()

  bran.pen(fillcolor="black", pencolor="red", pensize=10)

if __name__ == '__main__':
  main()