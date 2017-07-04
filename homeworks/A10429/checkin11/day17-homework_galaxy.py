#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
def main():
  # simulates motion of Mercury, Venus, Earth, and Mars
  import turtle

  mercury = turtle.Turtle()
  venus = turtle.Turtle()
  earth = turtle.Turtle()
  mars = turtle.Turtle()
  mercury.shape('circle')
  venus.shape('circle')
  earth.shape('circle')
  mars.shape('circle')
  mercury.pu()
  venus.pu()
  earth.pu()
  mars.pu()
  mercury.sety(-58)
  venus.sety(-108)
  earth.sety(-150)
  mars.sety(-228)
  mercury.pd()
  venus.pd()
  earth.pd()
  mars.pd()
  mars.speed(0)
  venus.speed(0)
  earth.speed(0)
  mars.speed(0)
  for i in range(360):
    mercury.circle(58, 7.5)
    venus.circle(108, 3)
    earth.circle(150, 2)
    mars.circle(228, 1)

if __name__ == '__main__':
    main()