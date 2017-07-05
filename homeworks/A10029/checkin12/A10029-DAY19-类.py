#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zi le

class People():
	def __init__(self,name,location):
		self.name=name
		self.location=location

	def hungary(self):
		print '来自%s的%s饿了 '%(self.location,self.name)

	def eat(self,food):
		print '%s吃了%s '%(self.name,food)

	def sleep(self,time):
		print '%s去睡了 %d 个小时 '%(self.name,time)


def main():
	zi_le=People(' 梓乐 ',' 郑州 ')
	zi_le.hungary()
	zi_le.eat(' 烤全羊 ')
	zi_le.sleep(3)


if __name__=='__main__':
	main()
