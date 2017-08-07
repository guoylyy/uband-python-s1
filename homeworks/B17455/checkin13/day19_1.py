#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

class Swimmer(object):
	"""docstring for ClassName"""
	def __init__(self, name, category,rank):
		self.name = name
		self.category = category
		self.rank = rank
		# super(ClassName, self).__init__()
		# self.arg = arg
		
	def competition(self):
		print '%s ranked %s in %s during the 17th FINA World Championships' % (self.name,self.rank,self.category)

def main():
	SunYang = Swimmer('SunYang', 'Free Style', 'First')
	SunYang.competition()


if __name__ == '__main__':
	main()




# class Fish():

# 	def __init__(self, name, location):
# 		self.name = name
# 		self.location = location
# 		# super(Fish, self).__init__()
# 		# self.arg = arg

# 	def jump(self):
# 		print '----------'
# 		print '有一个%s 正在 %s 活动' %(self.name, self.location)