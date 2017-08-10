#!/usr/bin/python
# -*- coding: utf-8 -*-

class Cat():
	"""docstring for Cat"""
	def __init__(self, name):
		self.name = name

	def jump(self,height):
		print 'The cat named %s jumped %d meters' %(self.name,height)

	def meow(self,times):
		print 'The cat meowed %d times' %(times)

def main():
	cici = Cat('cici')
	cici.jump(1)
	cici.meow(3)

if __name__ == '__main__':
	main()
