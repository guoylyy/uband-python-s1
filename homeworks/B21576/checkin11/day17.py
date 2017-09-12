#!/usr/bin/python
#-*-coding:utf-8-*-
#@author:suancaiyu

# 学习内容：  断续学习库的导入和方法的使用  
# 根据乌龟的运动轨迹画出各种图形

import turtle

def main():
  windows = turtle.Screen()  #设置画面
  windows.bgcolor('blue')   #背景色

#生成一个黄色的乌龟
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('yellow')

  bran.speed(1)
#生成一个黑色乌龟
  peter=turtle.Turtle()
  peter.shape('turtle')
  peter.color('black')

  for i in range(1,10):
  
    bran.forward(100)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
    bran.forward(100)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
  
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
