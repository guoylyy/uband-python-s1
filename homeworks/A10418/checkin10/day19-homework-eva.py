#!/usr/bin/python
# -*- coding: utf-8 -*-


class Fish():
	def __init__(self, name, location):

		self.name = name
		self.location = location

	def jump(self):
		print '来自 %s 的鱼 %s 开始跳起来了' %(self.location, self.name)

class Bird():
	def __init__(self, name):
		self.name = name

	def fly(self, height):
		print '%s 飞了 %d 米'%(self.name, height)

	def down(self):
		print '%s 摔死了'%(self.name)

class Dog():
	def __init__(self, name, kind):
		self.name=name
		self.kind=kind

	def run(self):
		print '小明回到家，他的宠物狗 %s 犬 %s 奔向他'%(self.kind, self.name)
	def jump(self):
		print '%s 看到小明非常开心，在小明脚边不停的蹦跳'%(self.name)
	def eat(self,meat):
		print '小明抱起 %s 走向厨房，喂它 %s '%(self.name, meat)
	def bark(self,times):
		print '%s 非常满意，高兴的叫了 %d 声'%(self.name, times)



def main():
	# angle=Bird('angle')
	# angle.fly(800)
	# angle.down()
	
	# bubu=Fish('bubu', 'Shanghai')
	# bubu.jump()

	meimei=Dog('meimei', '贵宾')
	meimei.run()
	meimei.jump()
	meimei.eat('pork')
	meimei.bark(3)


if __name__ == '__main__':
	main()