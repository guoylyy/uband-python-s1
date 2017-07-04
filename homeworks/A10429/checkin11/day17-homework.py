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
  twin = turtle.Turtle()
  twin.shape('turtle')
  twin.color('pink')
  twin.speed(1)
  twin.circle(20,360)
  bran.shape('turtle')
  bran.color('yellow')
  #开始你的表演
  #设置turtle的起始位置
  bran.setpos(0,-180)
  print bran.position()
  #画圆
  bran.home()
  bran.speed(1)
  bran.circle(80, 360)
  #画圆点
  bran.home()
  bran.setheading(90)
  bran.dot()
  bran.fd(80); bran.dot(20, "pink"); bran.fd(80)
if __name__ == '__main__':
  main()