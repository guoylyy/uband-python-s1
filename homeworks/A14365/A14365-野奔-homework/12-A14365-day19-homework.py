#!/usr/bin/python
# -*- coding: utf-8 -*-


class girlfriend():
	def __init__(self,name):
		self.name = name
		


	def kiss(self,time1):
		print '%s的女朋友很高兴，亲了他 %d 分钟 ' %(self.name,time1)
	def kick(self,time2):
		print '%s的女朋友不开心，踢了他 %d 分钟' %(self.name,time2)
	def sajiao(self,time3):
		print '%s的女朋友撒娇，要抱抱 %d 分钟' %(self.name, time3)

def main():
	Leo = girlfriend('Leo')
	Leo.kiss(5)
	Leo.kick(6)
	Leo.sajiao(10)

if __name__ == '__main__':
	main()