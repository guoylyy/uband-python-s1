#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tingting

class test():
	def __init__(self, name,which_school, which_class):
		self.name = name
		self.which_school = which_school
		self.which_class = which_class
		
		
	def sort(self):
		print '%s的%s参加了%s考试' % (self.which_school, self.which_class, self.name)
	
				
def main():
		translation = test('translation','一中','3班')
		translation.sort()	     
if __name__ == '__main__':
	main()
