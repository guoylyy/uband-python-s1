#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: qianchang

import turtle
  #设置一个画面
windows = turtle.Screen()
  #设置背景
windows.bgcolor('blue')
  #生成一个黄色乌龟
turtle.Turtle()
turtle.shape('turtle')
turtle.color('yellow')
  #设置速度
turtle.speed(1)
  #走几步
for i in range(1,10):
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    turtle.forward(100)
    turtle.right(90)
    turtle.forward(150)
    turtle.right(90)
    
import time
#格式化时间
# %Y-%m-%d 年-月-日 
# %A/%a %B/%b 星期 月份（英文缩写）
# %H:%M:%S 时：分：秒
localtime = time.asctime( time.localtime(time.time()) )
print "本地时间为", localtime
print time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
print time.strftime("%a %b %d %H:%M:%S %Y", time.localtime()) 

import calendar

cal = calendar.month(2016, 6)
print "以下输出2016年6月份的日历:"
print cal; 

