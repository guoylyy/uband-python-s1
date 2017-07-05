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
  arya = turtle.Turtle()
  sansa = turtle.Turtle()
  bran.shape('turtle')
  bran.shapesize(5,5,12)
  bran.color('yellow')
  bran.tilt(90)

  arya.shape('arrow')
  arya.color('red')
  sansa.shape('circle')
  sansa.color('black')
  
  #设置速度
  #设置速度
  bran.speed(1)
  arya.speed(1)
  sansa.speed(1)
  arya.penup()
  arya.setpos(100,0)
  arya.pendown()
  sansa.penup()
  sansa.setpos(-100,0)
  sansa.pendown()
  arya.circle(100)
  bran.circle(100)
  sansa.circle(100)
  
if __name__ == '__main__':
  main()