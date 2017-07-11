#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: chendasuan
import turtle

def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('white')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.dot(50,'yellow')
  #设置速度
  bran.speed(1)
  #走几步
  for i in range(1,6):
    bran.forward(100)
    bran.right(90)
    bran.backward(150)
    bran.lt(90)
    bran.circle(90,100,10)
    print bran.pos()

    
  #停下来

if __name__ == '__main__':
  main()