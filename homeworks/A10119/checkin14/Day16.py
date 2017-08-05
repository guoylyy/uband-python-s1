#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

import turtle#从外部把这个东西引入进来

def main():
    #设置一个画面
    windows = turtle.Screen()

    #设置背景
    windows.bgcolor('pink')

    #生成一个绿色乌龟
    bran = turtle.Turtle()
    bran.shape('turtle')
    bran.color('green')
    #设置速度
    bran.speed(1)
    #走几步
    for i in range(1,100):#走10次，试过这里i可以换成其他字母也没关系
      bran.forward(i)
      bran.left(50)
    #注释：ctrl +/ & command +/
    #停下来
if __name__ == '__main__':
  main()