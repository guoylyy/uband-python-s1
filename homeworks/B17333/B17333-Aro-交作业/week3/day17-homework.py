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
  turtle.reset()
  turtle.shape("circle")
  turtle.shapesize(5,2)
  turtle.settiltangle(45)
  turtle.fd(50)
  turtle.settiltangle(-45)
  turtle.fd(50)
  #开始你的表演
  bran.speed(1)
  bran.circle(50, 360, 100)

if __name__ == '__main__':
  main()