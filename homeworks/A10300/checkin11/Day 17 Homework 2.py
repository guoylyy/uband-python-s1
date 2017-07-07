# -*- coding: utf-8 -*-
# @author: Baoshi
import turtle

import time
turtle.color("purple")
turtle.shape('turtle')
turtle.pensize(8)
turtle.goto(0,0)
turtle.speed(1)


for i in range(6):
 turtle.forward(100)
 turtle.right(144)
turtle.up()
turtle.forward(100)
turtle.goto(-150,-120)
turtle.color("black")
turtle.write("Done")
time.sleep(4)
 

if __name__ == '__main__':
  main()