#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: qianchang

import turtle
def main():
    windows = turtle.Screen()
    windows.bgcolor('black')
    bran = turtle.Turtle()
    bran.shape('turtle')
    bran.color('yellow')
    bran.speed(1)
    bran.setx(40)
    bran.sety(40)
    bran.dot(20, "blue")
    bran.home()
    bran.setx(-40)
    bran.sety(40)
    bran.dot(20, "blue")
    bran.home()
    bran.setx(-40)
    bran.sety(-40)
    bran.dot(20, "blue")
    bran.home()
    bran.setx(40)
    bran.sety(-40)
    bran.dot(20, "blue")
    bran.home()

if __name__ == '__main__':
  main()
