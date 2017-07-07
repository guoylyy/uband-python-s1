#!/usr/bin/python
# -*- coding: utf-8 -*


class cat(object):
	"""docstring for cat"""
	def __init__(self, color, name, location):
		super(cat, self).__init__()
		self.color = color
		self.name = name
		self.location = location

	def lie(self):
		print "来自%s的%s色小猫%s懒洋洋地躺着" %(self.location, self.color, self.name)
		
		


def main():
	ivy = cat('yellow', 'ivy', 'ningbo')
	ivy.lie()


if __name__ == '__main__':
  main()