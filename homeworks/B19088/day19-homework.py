#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Winnie

class Fish():
	def __init__(self,name,location):
		self.name = name
		self.location = location

	def jump(self):
		print '来自 %s 的鱼 %s 开始跳起来啦'%(self.location,self.name)

class Bird():
	def __init__(self,name):
		self.name = name

	def fly(self,height):
		print '%s 飞了 %d 米' %(self.name, height)

	def down(self):
		print '%s 摔死了' %(self.name)

class Student():
	def __init__(self,name):
		self.name = name

	def exam(self, performance):
		print '%s 作业得了%d 分' %(self.name,performance)

def main():
	allen = Fish('allen','shanghai')
	allen.jump()


	hellen = Bird('hellen')
	hellen.fly(800)
	hellen.down()

	winnie = Student('winnie')
	winnie.exam(100)








if __name__ == '__main__':
  main()


