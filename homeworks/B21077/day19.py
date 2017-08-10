##!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

class Fish():
	def __init__(self,location,name):#定义
		self.name=name
		self.location=location
	def jump(self):
		print' 来自%s的鱼%s开始跳起来了 '%(self.location,self.name)
def main():
	allen= Fish('shanghai','allen')
	allen.jump()
if __name__ == '__main__':
	main()


class Children():
	def __init__(self,dad,mom):
		self.dad=dad
		self.mom=mom
	def parents(self):
		print'孩子的爸爸是%s,妈妈是%s'%(self.dad,self.mom)
def main():
	child=Children('teacher','doctor')
	child.parents()
if __name__ == '__main__':
 		main() 	