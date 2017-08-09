#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import turtle



def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('brown')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('green')
  turtle.onclick('turn')
  #设置速度
  bran.speed(3)

 
  #走几步
  for i in range(1,1000):
    bran.forward(i)
    bran.right(56)
    bran.pensize(3)
    turtle.up()
    turtle.dot(20,'white')
   


   













  
 
  #停下来


if __name__ == '__main__':
  main()