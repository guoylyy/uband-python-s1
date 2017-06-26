#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: bettyyan
import turtle

def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('blue')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('circle')
  bran.shapesize(1.1)
  bran.color('yellow','red')
  #开始你的表演
  # turtle.circle(50,90)
  # turtle.circle(60,180)
  # turtle.circle(70,270)
  # turtle.circle(80)
  bran.speed(2)
  bran.pensize(2)
  bran.position()
  (-100.00,300.00) 
  bran.begin_fill()
  for i in range(10):
    bran.forward(100)
    bran.right(120) 
  bran.end_fill() 
  joe = bran.clone()
  joe.shape('turtle')
  joe.shapesize()
  for i1 in range(10):
  	joe.circle(50,360,1000)

if __name__ == '__main__':
  main()