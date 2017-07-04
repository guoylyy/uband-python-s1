#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: shangxindepidan

import turtle

def main():
  #设置一个画面
  window = turtle.Screen()
  #设置背景
  window.bgcolor('purple')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('yellow')
  #设置速度
  bran.speed(1)
  #走几步
  for i in range(1,6):
    bran.forward(100)
    bran.right(144)
  #停下来

if __name__ == '__main__':
  main()