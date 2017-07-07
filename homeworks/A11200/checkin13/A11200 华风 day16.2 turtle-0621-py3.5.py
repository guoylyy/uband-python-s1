#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Huafeng
import turtle   # 调用模块
from turtle import *

def main():
  #设置画面
  windows = turtle.Screen()
  
  color('red','yellow')     # 定义颜色
  begin_fill()              #开始
  while True:                # 当为真时循环
    forward (100)             #向前走200步
    left (170)                #向左走170
    if abs (pos ()) < 1:        #如果 
       break                    #跳出
  end_fill ()
  
  #设置背景
  windows.bgcolor('green')
  #生成一个红色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('red')
  #设置速度
  bran.speed(1)
  bran.forward(100)
  bran.circle(100,360,10)
  #走几步
  for i in range(1,3):
    bran.forward(150)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
  #停下来
  done ()
if __name__ == '__main__':
  main()