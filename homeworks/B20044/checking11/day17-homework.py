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
  bran.speed(3)
  #开始你的表演
  #for i in range(1,20):#注意要加range，中间是,
  bran.fillcolor('red')  


  bran.fill(True)
  for i in range(1,10):
      bran.speed(20)
      bran.circle(120, 360)
      bran.right(45)
      bran.circle(120, 360)
      bran.right(45)
      bran.circle(120, 360)
  bran.fill(False)

  bran.hideturtle()

  
if __name__ == '__main__':
  main()