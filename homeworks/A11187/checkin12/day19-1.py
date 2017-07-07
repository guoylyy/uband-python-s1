#!/usr/bin/python
# -*- coding: utf-8 -*
 
class Girl():
	def __init__(self, name, location):
		self.name = name
		self.location = location
 
	def jump(self):
		print 'girl %s that comes from %s begins to jump' %(self.name, self.location)

def main():
	sunnie = Girl('sunnie', 'changchun')
	sunnie.jump()

if __name__ == '__main__':
	main()
 