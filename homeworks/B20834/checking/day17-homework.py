#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
import turtle

def main():
 
  windows = turtle.Screen()
  
  windows.bgcolor('yellow')
 
  ninjia = turtle.Turtle()
  ninjia.shape('arrow')
  ninjia.color('black')
  ninjia.dot(5,'red')

  for i in range(1,10):
    ninjia.circle(120,180)


if __name__ == '__main__':
  main()