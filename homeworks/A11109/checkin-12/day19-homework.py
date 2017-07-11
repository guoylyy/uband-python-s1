#!/usr/bin/python
# -*- coding: utf-8 -*

class Creditcard():
	def __init__(self, name, location):
		self.name = name
		self.location = location

	def store(self):
		print '来自 %s 的信用卡 %s 可以存钱' %(self.location, self.name)

	def withdraw(self, limit):
		print '信用卡 %s 可以使用免费额度 %d 元' %(self.name, limit)

def main():
	visa = Creditcard('visa', 'qingdao')
	visa.store()
	visa.withdraw(2000)

if __name__ == '__main__':
  main()