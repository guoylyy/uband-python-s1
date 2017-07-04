#! /bin/usr/python
#-*- coding:utf-8 -*-
#@author:SKY
#

class Teacher():
	def __init__(self,name,age,sub):
		self.name=name
		self.age=age
		self.sub=sub
	def info(self):
		print '%s 老师，今年%d 岁，教%s ' % (self.name,self.age,self.sub)
class Cat():
	def __init__(self,name):
		self.name=name

	def run(self):
		print '小猫 %s 跑的很快！' % (self.name)

def main():
	teacher=Teacher("王刚",34,"数学")
	cat=Cat("tom")
	teacher.info()
	cat.run()

if __name__ == '__main__':
	main()