#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Huafeng
import turtle   # 调用模块

def main():
  #设置画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('green')
  #生成一个红色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('red')
  #设置速度
  bran.speed(1)
  bran.circle(100,360,5)
  #走几步
  #for i in range(1,6):
    # bran.forward(150)
    # bran.right(90)
    # bran.forward(150)
    # bran.right(90)
    # bran.forward(150)
    # bran.right(90)
    # bran.forward(150)
    # bran.right(90)
  #停下来

if __name__ == '__main__':
  main()