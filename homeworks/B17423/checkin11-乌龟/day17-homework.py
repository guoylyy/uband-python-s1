#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: seiya
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
  #开始你的表演
  bran.circle(50,360)
  bran.turtlesize(1,1,3)  #乌龟大小

  #bran.home()
  bran.setx(300)
  bran.sety(100)   #设置乌龟为止
  bran.seth(90)    #设置乌龟开始的角度
  bran.begin_poly()  #开始记录多边形顶点
  bran.fd(100)  #forward
  bran.left(20)
  bran.fd(30)
  bran.left(60)
  bran.fd(50)
  bran.end_poly()  #停止记录多边形顶点，并将其与第一个顶点相连
  #p=turtle.get_poly()
  turtle.addshape('triangle',((5,-3),(0,5),(-5,-3)))  #添加形状


  sea = turtle.Turtle()
  sea.shape('triangle')   #改成刚加入的形状
  sea.color('red')
  sea.setpos(-30,100)    #设置起始位置
  sea.circle(50,360,200)
  # for i in range(1,10):
  #   sea.forward(10)
  #   sea.right(9)
  #   sea.forward(15)
  #   sea.right(9)
  #   sea.forward(10)
  #   sea.right(9)
  #   sea.forward(15)
  #   sea.right(9)



if __name__ == '__main__':
  main()