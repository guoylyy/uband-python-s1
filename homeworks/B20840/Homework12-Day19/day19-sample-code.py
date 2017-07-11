#!/usr/bin/python
# -*- coding: utf-8 -*
#Author:B20840

class Fish():
	def __init__(self, name, location):
		self.name=name
		self.location=location

	def jump(self):
		print '来自 %s 的鱼 %s 开始跳起来了' %(self.location, self.name)

class dog():
	"""docstring for ClassName"""
	def __init__(self, name, color, tp):
		self.name = name
		self.color = color
		self.tp = tp

	def run(self):
		print '一只叫 %s 的 %s 色 %s 大狗跑出去了' %(self.name, self.color, self.tp)
		
class bird():
	def __init__(self, name, color):
		self.name=name
		self.color=color

	def fly(self):
		print '一只叫 %s的 %s 小鸟正要飞起来' %(self.name, self.color)


		
def main():
	allen = Fish('allen', 'shanghai')
	allen.jump()

	nymenia = dog('nymenia', '黄色', '金毛')
	nymenia.run()

	cookie = bird('cookie', '灰色')
	cookie.fly()



if __name__ == '__main__':
	main()