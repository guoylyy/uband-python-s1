#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: caramel

class Fish():
	def __init__(self, name, location):
		self.name = name
		self.location = location
	def jump(self):
		print 'a fish %s, coming from %s, starts to jump up.'% (self.name, self.location)

class Cat():
	def __init__(self, name):
		self.name = name
	def catch(self, number):
		print 'a cat named "%s" catches %d mice.'% (self.name, number)

class Eagle():
	def __init__(self, name):
		self.name = name
	def eat(self, number):
		print 'a eagle named "%s" ate %d big snakes last week.'% (self.name, number)

def main():
	allen = Fish('allen', 'shanghai')
	allen.jump()

	tiger = Cat('tiger')
	tiger.catch(2)

	hero = Eagle('hero')
	hero.eat(4)

if __name__ == '__main__':
  main()