#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: seiya

class Person():
	"""docstring for Person"""
	def __init__(self, name, age):
		# super(Person, self).__init__()
		self.name = name
		self.age = age

	def introduction(self):
		print ("Hello, My name is %s, I am %d years old. Thank you!" % (self.name, self.age))


def main():
	seiya = Person("seiya", 23)
	seiya.introduction()

if __name__ == '__main__':
	main()