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
  bran.speed(3)
  bran.circle(100,180)
  bran.stamp()
  bran.circle(100,180)
  bran.fd(200)
  print bran.pos()
  bran.rt(90)
  bran.dot(20,'white')
  bran.fd(200)

if __name__ == '__main__':
  main()