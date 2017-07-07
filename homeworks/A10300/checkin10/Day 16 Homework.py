# -*- coding: utf-8 -*-
# @author: Baoshi
import turtle

def main():
  
  windows = turtle.Screen()
  windows.bgcolor('blue')
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('yellow')
  bran.speed(1)
 
  for i in range(1,10):
    bran.forward(100)
    bran.left(120)
    bran.forward(100)
    bran.right(60)
    bran.backward(100)
    
 

if __name__ == '__main__':
  main()