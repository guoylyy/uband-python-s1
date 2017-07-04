#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Huafeng

import turtle   # 调用模块
from turtle import *
class Cat():
  def __init__(self, name, location):
    self.name = name
    self.location = location

  def run(self):
    print ('来自 %s 的猫 %s 高兴的跑了' %(self.location, self.name))

  def stop(self):
    print ('%s 跑到我家里来了' % (self.name))

def main1():
  ally = Cat('ally', 'hunan')
  ally.run()
  ally.stop()
  windows1 = turtle.Screen()
  windows1.bgcolor('green')           #背景为绿色
  
  bran = turtle.Turtle()           #为乌龟赋名
  bran.shape('turtle')             #乌龟的形状
  bran.color('red')                #乌龟的颜色
  bran.speed(1)                   #设置乌龟走的速度
  bran.circle(100,360,10)         # 乌龟走圆形，直径100,360度，10个线段
  for i in range(0,2):             #乌龟用1的速度循环3次  0 1 
    bran.forward(150)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
    bran.forward(150)
    bran.right(90)

if __name__ == '__main__':
  main1()
 