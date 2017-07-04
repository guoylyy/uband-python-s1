#!/usr/bin/python
# -*- coding: utf-8 -*
# @author: IPLAY

class Rabbit():
	def __init__(self, name):
		self.name = name
 	def jump(self, color, location, height):
		print ' The  %s rabbit, which is from %s, is called %s. It jumps well, and it can jump about %d meters.' % (color, location, self.name, height)
 	
def main():
	eric = Rabbit('eric')
	eric.jump('white', 'hangzhou', 2)
	
	

if __name__ == '__main__':
	main()