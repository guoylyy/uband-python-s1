#! usr/bin/python
# -*- coding: utf-8 -*-
# @author:Emma

class Fish():
	def __init__(self,name,location):
		self.name = name
		self.location = location
	def jump(self):
		print ' %s fish %s start to jump' %(self.location,self.name)

def main():
	allen = Fish('allen','shanghai')
	allen.jump()

class Cat():
	def __init__(self,name,location,color,food):
		self.name = name
		self.location = location
		self.color = color
		self.food = food
	def play(self):
		print 'a %s cat named %s from %s likes to play with his two owners. ' %(self.color,self.name,self.location)
	def eat(self):
		print '%s always eat %s for food.' %(self.name,self.food)


def homework():
	MrSakamoto = Cat('MrSakamoto','Japan','black','fish')
	MrSakamoto.play()
	MrSakamoto.eat()
	

if __name__ == '__main__':
	homework()