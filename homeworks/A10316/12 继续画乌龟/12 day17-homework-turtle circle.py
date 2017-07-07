#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: sanlianyin
import turtle

def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('blue')
  # 生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('yellow', 'red')   #乌龟的线条和颜色会不一样
  #开始你的表演
   
  bran.speed(1)
  bran.circle(120, 360, 100)
  

  bran.color('red','red')
  bran.speed(10)
  for i in range(1, 100):

    bran.forward(25)
    bran.right(45)
    bran.forward(90)
    bran.right(65)
    bran.forward(20)
    bran.right(45)
    bran.forward(90)
    bran.right(65)
    bran.forward(20)



if __name__ == '__main__':
  main()
  