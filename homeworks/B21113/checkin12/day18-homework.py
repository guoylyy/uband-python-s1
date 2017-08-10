#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: eros

class Dog():
  def __init__(self,name,location,action ):
 	self.name = name
	self.location = location
	self.action = action

  def run(self):
	print '来自 %s 的狗 %s 开始 %s 起来了' %(self.location, self.name,self.action)

def main():
	wangcai = Dog('旺财','昆明','跳')
	wangcai.run()

if __name__ == '__main__':
 	main()