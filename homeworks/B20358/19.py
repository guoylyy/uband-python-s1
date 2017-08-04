#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Anna

class Cat():
	def __init__(self, name, location):
		self.name = name
		self.location = location

	def clamp(self):
		print '来自 %s 的猫 %s 开始爬起了树' %(self.location, self.name)


def main():
	star = Cat('star', 'jiuhuashan')
	star.clamp()

if __name__ == '__main__':
	main()