#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import turtle

def main():
  #设置一个画面
  #设置背景
  #生成一个黄色乌龟
  windows = turtle.Screen()
  windows.bgcolor('purple')
  jack = turtle.Turtle()
  jack.shape('turtle')
  jack.color('blue')
  jack.speed(3)

  #开始你的表演
  for i in (1,100):
    jack.forward(100)
    jack.left(90)
    jack.forward(100)
    jack.left(90)
    jack.forward(100)
    jack.left(90)
if __name__ == '__main__':
  main()