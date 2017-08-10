#!/usr/bin/python
#-*- coding: utf-8 -*-

class human():
	def __init__(self,name,location):
		self.name=name
		self.location=location

	def eat(self):
		print '来自%s的%s吃了碗大米饭'%(self.location,self.name)
	
	def sleep(self):
		print '来自%s的%s开始打起了呼噜'%(self.location,self.name)




def main():
	allen = human('allen','shenzhen')
	allen.eat()
	karen = human('karen','dalian')
	karen.sleep()

if __name__ == '__main__':
	main()