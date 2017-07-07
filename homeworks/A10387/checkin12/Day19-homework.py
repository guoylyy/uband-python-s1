#!/usr/bin/python
# -*- coding: utf-8 -*

class Beef():
	def __init__(self, name, price, comments):
		self.name = name
		self.price = price
		self.comments = comments
	def cook(self):
		print '%s牛肉买了%d元一斤，味道%s' % (self.name, self.price, self.comments)

	def electricShock(self):
		if self.price < 100:
			print '%s牛肉被电焦啦' % (self.name)
		else:
			print '%s牛活过来了！！！' % (self.name)

class Human():
	
	def __init__(self, name, status):
		self.name = name;
		self.status = status;
		print '%s is %s' % (self.name, self.status)
	def eat(self):
		if self.status == 'hungry':
			print '%s eats a beef steak.' % (self.name)
			self.status = 'full'
		else:
			print '%s is full. %s does not want to eat anything.' % (self.name, self.name)
			print '%s决定电击一下剩下的牛肉' % (self.name)
						
def main():
	Ann = Human('Ann', 'hungry')
	Ann.eat()
	Steak1 = Beef('神户', 500, '太棒了！')
	Steak1.cook()
	Ann.eat()
	Steak2 = Beef('汕头', 50, '很棒！')
	Steak2.electricShock()

if __name__ == '__main__':
	main()



