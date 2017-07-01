#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import turtle

def main():
  #设置一个画面
  drawing = turtle.Screen()
 
  #设置背景
  drawing.bgcolor("black")

  #生成一个黄色乌龟
  animal = turtle.Turtle()
  animal.shape("turtle")
  animal.color("white")

  #设置速度
  animal.speed(1)

  #走几步
  for i in range(1,100):
    animal.forward(100)
    animal.right(90)


  #停下来

if __name__ == '__main__':
  main()