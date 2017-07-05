#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Anqi
import turtle

def main():
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('grey')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('pink')
  #设置速度
  bran.speed(4)
  #走几步
  for i in range(1,100):
    bran.forward(100)
    bran.right(90)
    bran.forward(100)
    bran.right(90)
    bran.forward(100)
    bran.right(90)
    bran.forward(100)
    bran.right(90)
  #停下来

if __name__ == '__main__':
  main()