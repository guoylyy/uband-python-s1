#!/usr/bin/python
# -*- coding: utf-8 -*-

class Dog():
	def __init__(self,name):
		self.name = name
	

	def run(self):
		print '我家的狗 %s 开始跑了起来 ' % (self.name)

	



def main():
	lulu = Dog('lulu')
	lulu.run()
	


if __name__ == '__main__':
	main()			