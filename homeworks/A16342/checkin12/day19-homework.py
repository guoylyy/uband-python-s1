#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yan

class dog():
	def __init__(self,name):
		self.name = name

	def eat(self,food):
		print '%s吃了%s' % (self.name, food)

	def bark(self):
		print '%s朝你叫了一声' % (self.name)

	def wag(self):
		print '%s摇了摇尾巴' % (self.name)
	
def main():
	Bai = dog('小白')
	Bai.wag()
	Bai.eat('一根骨头')
	Bai.bark()

if __name__ == '__main__':
	main()

