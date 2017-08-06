#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yuanzi
import turtle  
import time  
def main():
  #设置一个画面
  windows = turtle.Screen()
  #设置背景
  windows.bgcolor('pink')
  #生成一个黄色乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('red')
  
  
  turtle.color("purple")  
  turtle.pensize(5)  
  turtle.goto(0,0)  
  turtle.speed(10)  
  
  for i in range(1,6):  
    turtle.forward(100)  
    turtle.right(144)  
  turtle.up()  
  turtle.forward(100)  
  turtle.goto(-150,-120)  
  turtle.color("red")  
  turtle.write("Done")  
  time.sleep(30)

if __name__ == '__main__':
  	main()  