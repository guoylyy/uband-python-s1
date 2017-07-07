#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Casey

import turtle

def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('black')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('white')
  
  turtle.home()
  turtle.dot()
  turtle.fd(50); turtle.dot(20, "blue"); turtle.fd(50)
  turtle.position()
  (100.00,-0.00)
  turtle.heading()
0.0

if __name__ == '__main__':
  main()