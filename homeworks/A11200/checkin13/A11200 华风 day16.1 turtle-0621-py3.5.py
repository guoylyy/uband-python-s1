#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Huafeng
import turtle   # 调用模块
from turtle import *

def main():
  #设置画面
  windows = turtle.Screen()
  
  color('red','yellow')
  begin_fill()
  while True:
    forward (200)
    left (170)
    if abs (pos ()) < 1:
       break
  end_fill ()
  done ()
 
  

if __name__ == '__main__':
  main()