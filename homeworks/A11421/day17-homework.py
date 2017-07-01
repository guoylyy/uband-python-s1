#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import turtle



def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('black')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color("white")
  bran.pencolor("yellow")
  #开始你的表演
  bran.speed(10)
  bran.circle(100,360,100)
  # class MyTurtle():
  #   def glow(self,x,y):
  #     self.fillcolor("white")
  #   def unglow(self,x,y):
  #     self.fillcolor("")

  # turtle = MyTurtle()
  # turtle.onclick(turtle.glow)     # clicking on turtle turns fillcolor red,
  # turtle.onrelease(turtle.unglow) 



  

if __name__ == '__main__':
  main()