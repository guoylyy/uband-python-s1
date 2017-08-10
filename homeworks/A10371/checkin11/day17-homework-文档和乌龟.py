#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yuanzi
import turtle
import time
def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('pink')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('red')
  #开始你的表演  
  turtle.home()
  turtle.dot()
  for i in range(1,10):
  
    turtle.fd(50)
    turtle.dot(30,"blue")
    turtle.fd(50)
    turtle.position()
    (100.00,-0.00)
    turtle.heading()
    0.0
    turtle.fd(50)
    turtle.right(90)
    turtle.fd(50)

  turtle.stamp()
  11
  turtle.fd(50)

  time.sleep(10)



if __name__ == '__main__':
  main()