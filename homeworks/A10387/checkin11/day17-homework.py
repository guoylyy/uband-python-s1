#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import turtle
import math

def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('black')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  skii = turtle.Turtle()

  bran.shape('turtle')
  skii.shape('turtle')
  bran.color('lightsteelblue')
  skii.color('pink')
  #开始你的表演

  bran.speed(1)
  skii.speed(1)
  bran.circle(50, 360, 100)
  skii.circle(100, 360, 100)
  skii.left(45)
  skii.forward(50*math.sqrt(2))
  skii.left(45)
  skii.circle(25, 180, 100)
  skii.left(180)
  skii.circle(25, 180, 100)
  skii.left(45)
  skii.forward(50*math.sqrt(2))

  bran.left(45)
  bran.forward(100*math.sqrt(2))
  bran.left(45)
  bran.circle(50, 180, 100)
  bran.left(180)
  bran.circle(50, 180, 100)
  bran.left(45)
  bran.forward(100*math.sqrt(2))

  bran.clear()
  skii.clear()

  skii.right(180)
  for i in range(1,12):
    bran.circle(50, 540, 100)
    bran.right(30)

  for i in range(1,12):
    skii.circle(50, 540, 100)
    skii.right(30)

  bran.clear()
  skii.clear()
  skii.width(6)
  skii.speed(3)
  for i in range(1,16):
    skii.circle(100, 360, 100)
    skii.right(30)
    

if __name__ == '__main__':
  main()