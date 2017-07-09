#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: chendasuan
import turtle

def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('green')
  #生成一个白色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('white')
  #设置速度
  bran.speed(1)
  #走几步

  for i in range(1,5):
    bran.forward(100)
    bran.right(90)#角度
    bran.forward(150)
    bran.right(45)#角度
    bran.forward(100)
    bran.right(45)#角度
    bran.forward(200)
    bran.right(90)





if __name__ == '__main__':
  main()