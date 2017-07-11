#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: lightningLUO



class dog():
	def __init__(self, name, location):
		self.name = name
		self.location = location
	def run(self, speed):
		print'来自%s的%s每秒可以跑%s米' %(self.location, self.name, speed)

def main():
	Mike = dog('Mike','US')
	Mike.run(5)


if __name__ == '__main__':
	main()
