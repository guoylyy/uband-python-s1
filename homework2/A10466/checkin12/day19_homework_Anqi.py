#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Anqi
class cat():
	def __init__(self, name,age):
		self.name=name
		self.age=age

 	def speak(self):
 		print'名叫 %s 的猫 %s 岁会说话了' %(self.name,self.age)

def main():
	miao=cat('miao','3')
	miao.speak()

if __name__ == '__main__':
  main()