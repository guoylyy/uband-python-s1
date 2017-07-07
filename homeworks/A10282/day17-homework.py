#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 233
import turtle

def main1():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('blue')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('yellow')
  #开始你的表演
  bran.speed(1)
  bran.circle(50,360,1000)    #半径，角度，步数,步数越多画出来的圆就会更圆。
if __name__ == '__main__':
  main1()


def main2():
  windows = turtle.Screen()
  windows.bgcolor('green')
  bran = turtle.Turtle()
  tp = turtle.pos()
  bran.setpos(60,30)
  bran.setpos((20,80))
if __name__ == '__main__':
  main2()