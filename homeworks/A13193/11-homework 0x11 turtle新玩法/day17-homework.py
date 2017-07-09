#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Pennsylvania
import turtle

def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('black')
  #生成一个白色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('white')
  #设置速度
  bran.speed(1)
  bran.circle(120, 720, 50)

if __name__ == '__main__':
  main()