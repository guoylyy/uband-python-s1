#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Huafeng

import turtle   # 调用模块
from turtle import *

def main1():

  windows1 = turtle.Screen()
  windows1.bgcolor('green')           #背景为绿色
  
  bran = turtle.Turtle()           #为乌龟赋名
  bran.shape('turtle')             #乌龟的形状
  bran.color('red')                #乌龟的颜色
  bran.speed(1)                   #设置乌龟走的速度
  bran.circle(100,360,10)         # 乌龟走圆形，直径100,360度，10个线段
  for i in range(0,3):             #乌龟用1的速度循环3次  0 1 2 
    bran.forward(150)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
    bran.forward(150)
    bran.right(90)

def main2():  
  windows2 = turtle.Screen()
  windows2.bgcolor('white')   
  ally = turtle.Turtle()           #为乌龟赋名
  ally.shape('turtle')             #乌龟的形状
  ally.color('blue')                #乌龟的颜色
  ally.speed(1)                   #设置乌龟走的速度
  ally.circle(100,360,10)         # 乌龟走圆形，直径100,360度，10个线段
  for i in range(0,3):             #乌龟用1的速度循环3次  0 1 2 
    ally.forward(150)
    ally.right(90)
    ally.forward(150)
    ally.right(90)
    ally.forward(150)
    ally.right(90)
    ally.forward(150)
    ally.right(90)

if __name__ == '__main__':
  main1()
  main2()