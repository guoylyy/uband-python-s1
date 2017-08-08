#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
# 

class Dog():
	def __init__(self,name,location):
	  self.name = name
	  self.location = location

	def shark(self):
		print '来自 %s 的狗 %s开始叫起来了' %(self.location,self.name)

class Bird():
  def __init__(self,name):
    self.name = name 

  def fly(self,height):
    print '%s 飞了 %d  米' %(self.name ,height) 

  def down(self):
  	print '%s 摔死了' %(self.name)

class Cat():
  def __init__(self,name):
    self.name = name 
    #self.distance = distance

  def run(self,distance):
    print '%s 听到狗的叫声，从 %d  米处跑过来看看' %(self.name ,distance) 

  def eat(self):
  	print '%s 把死鸟给吃了' %(self.name)


def main():
	angile = Bird('angile')
	angile.fly(800)
	angile.down()
	allen = Dog('allen','shanghai')
	allen.shark()
	sesa = Cat('sesa')
	sesa.run(15)
	sesa.eat()

if __name__ == '__main__':
  main()