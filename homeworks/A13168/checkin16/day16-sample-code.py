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
  #设置速度
  bran.speed(1)
  #走几步
  for i in range(1,10):
    bran.forward(100)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
    bran.forward(100)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
  #停下来

if __name__ == '__main__':
  main()