# -*- coding: utf-8 -*-
# @author: Baoshi
import turtle

def main():
  
  windows = turtle.Screen()
  windows.bgcolor('orange')
  bran = turtle.Turtle()
  bran.shape('turtle')
  bran.color('blue')
  astamp = turtle.stamp()
  turtle.fd(50)
  bran.speed(1)
  bran.circle(120,720)
 
  for i in range(1,10):
    bran.forward(100)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
    bran.forward(150)
    bran.right(90)
    turtle.clearstamp(astamp)
    
 

if __name__ == '__main__':
  main()