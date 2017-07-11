#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: vera

class Koala():
	def __init__(self, name):
		self.name = name

	def climb(self, height):
		print '%s 爬了 %d 米' %(self.name, height)

	def relax(self, minute):
		print '%s 休息了 %d 分钟' %(self.name, minute)

def main():
	mandy = Koala('mandy')
	mandy.climb(1)
	mandy.relax(10)

if __name__ == '__main__':
	main()