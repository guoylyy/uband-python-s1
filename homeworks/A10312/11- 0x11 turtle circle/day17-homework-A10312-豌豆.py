#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: wandou
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

  #circle
  bran.speed(1)
  bran.circle(45,360,66)
  
  bran.speed(1)
  bran.forward(80)
  bran.back(20)
  bran.right(90)
  bran.forward(80)
  bran.left(90)

  bran.goto(33)


if __name__ == '__main__':
  main()