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
  bran.speed(5)
  #开始你的表演
  for i in range(10):
    bran.setx(10*i)
    print bran.position()
    bran.circle(100,30*i)
    print bran.heading()
    print bran.position()


if __name__ == '__main__':
  main()