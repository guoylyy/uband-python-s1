#!/usr/bin/python
# -*- coding: utf-8 -*
# @author: Xiangwan

'''
类就是有相同行为的一段东西，里面包含了很多描述它行为的代码块。
类就是一个蓝图，定义了现实中的一些东西,如turtle定义了一直乌龟，每只乌龟都可以向左，向右，转圈等。
类需要实例化
'''

class Fish():#现实世界物质体的一个对应体，要把常见的功能等描述清楚就需要用到类
	def __init__(self, name, location):#init把鱼的信息初始化
	  self.name = name
	  self.location = location

	def jump(self):
		print '来自 %s 的鱼 %s 开始跳起来了  ' %(self.location, self.name)

class Rabbit():
	def __init__(self, name, location, goal, destination):
		self.name = name
		self.location = location
		self.goal = goal
		self.destination = destination

	def eat(self):
		print '来自 %s 的兔子 %s 爱吃 %s ' %(self.location, self.name, self.goal)
	def wander(self):
		print '%s 喜欢在 %s 散步 '% (self.name, self.destination)
	def count(self):
		print '%s 会在睡前数星星, '% (self.name);
		for i in range(1,11):
			print '%d 只星星' %(i)

def main():
	Judy = Rabbit('Judy Hopps','Africa', '胡萝卜', 'forests and fields')
	Judy.eat()
	Judy.wander()
	Judy.count()

if __name__ == '__main__':
	main()