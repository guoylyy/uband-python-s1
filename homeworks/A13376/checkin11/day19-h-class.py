#!/usr/bin/python
# -*- coding: utf-8 -*


class Dog():
	def __init__(self, name):
		self.name = name

	def run(self, meter):
		print '%s run %d meters' %(self.name, meter)
		
	def bite(self):
		print '%s can bite people' %(self.name)


def main():
	collins = Dog('Collins')
	collins.run(200)
	collins.bite()

if __name__ == '__main__':
	main()