#!/bin/sur/python
#-*-coding:utf-8 -*-
#@author:SKY
# 说明：红色小乌龟在下面旋转画出一朵花
# 绑定了窗口点击事件，点击屏幕出现一个自定义背景的乌龟，旋转出现
import turtle

windows=turtle.Screen()
windows.bgpic("2.gif")   #设置背景图片
windows.register_shape("timg.gif")
bran=turtle.Turtle()
bran.color("yellow")
bran.shape("timg.gif")
bran.hideturtle()  #隐藏乌龟

#画乌龟
def draw():
	for i in range(6):
		bran.showturtle()  #显示乌龟
		bran.stamp()  #复制乌龟
		bran.backward(60)
		bran.undo()  
		bran.right(90)

def gogogo(x,y):   #从窗口点击事件
	bran.up()      #不画线
	bran.goto(x,y)
	bran.down()		#画线
	draw()

def main():
	windows.onclick(gogogo)		#绑定点击事件
	t=turtle.Turtle()
	t.color("red")
	t.shape("turtle")
	t.goto(40,40)
	while 1:
		t.forward(100)
		t.right(70)

if __name__ == '__main__':
	main()

