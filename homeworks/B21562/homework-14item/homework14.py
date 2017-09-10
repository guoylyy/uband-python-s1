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
  bran = turtle.Turtle() #用bran变量，代替了turtle.turtle()
  bran.shape('turtle')
  bran.color('green')
  #开始你的表演
  bran.circle(50,720,100) #画圆
  turtle motion
  bran.forward(100) #前进
  print bran.position()#报告位置
  bran.fd(-100)
  bran.back(200)#后退
  # bran.bk(-200)
  # print bran.position()
  # print bran.heading()
  #bran.rt(45)
  #bran.fd(100)
  #bran.lt(90)
  #bran.bk(100)
  # bran.position()
  # print bran.position()
  # #print bran.heading()
  # #bran.goto(60.00,30.00)#移动到坐标点所在位置
  # #bran.setpos(200,80) #移动到坐标点所在位置
  # #bran.setx(10) #y坐标保持不变，x坐标+10
  # #bran.set7(10) #y坐标保持不变，x坐标+10
  # print bran.position()
  # bran.seth(90) #头部转向
  # print bran.heading() #不要忘了函数后面的括号
  # bran.home() #归位
  #print bran.heading()
  #for i in range(1,10):
    #bran.lt(9);bran.fd(50);bran.dot(10,"yellow");bran.rt(171);bran.fd(50)
  #  bran.fd(25);bran.lt(135);bran.fd(25);bran.lt(360-135)

  #bran.dot(size=None, *color)打一个小圆点，size：圆点大小，color，颜色，颜色记得要打引号
  # bran.fd(100)
  # bran.stamp()
  # astamp=bran.stamp()
  # print bran.position()
  # bran.fd(100)
  # bran.clearstamp(astamp)
  # print bran.position()
  
  




if __name__ == '__main__':
  main()