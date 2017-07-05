#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zi le
import turtle

def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置标题
  turtle.title('welcome to turtle home')
  #设置背景
  windows.bgcolor('blue')
  #生成一个黄色乌龟sandy
  sandy=turtle.Turtle()
  sandy.shape('turtle')
  sandy.color('yellow')
  #生成一个黑色乌龟peter
  peter=turtle.Turtle()
  peter.shape('turtle')
  peter.color('black')

  number_1=58
  sandy.speed(20)
  for i in range(6):
    sandy.forward(100)
    sandy.circle(number_1,360)
    sandy.left(120)
    sandy.forward(100)
    sandy.left(120)
    sandy.forward(100)
    sandy.left(60)


  peter.penup()
  peter.goto(0,-200)
  peter.pendown()
  peter.circle(200)
  
  peter.penup()
  peter.goto(0,-150)
  peter.pendown()
  peter.circle(150)
  
  peter.penup()
  peter.goto(0,-100)
  peter.pendown()
  peter.circle(100)
  
  peter.penup()
  peter.goto(0,-50)
  peter.pendown()
  peter.circle(50)
  



if __name__ == '__main__':
  main()