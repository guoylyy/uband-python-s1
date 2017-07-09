#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Qipajie

#注释的快捷键 ctrl+/


class Fish(): #定义了鱼这个类 大写  注意，在class括号内不要写变量
	def __init__(self,name,location): #把鱼的信息初始化，因为不同鱼名字，产地不一样   __要打2次   初始值时才引入变量
	
		# allen=Fish ('allen','shanghai')调用了这个函数
		self.name=name   			#实例化时把这些数据传进来，然后定义一个鱼
		self.location=location			

	def jump(self):  #可以定义鱼的一些行为 后面忘加：  引入self就行，不用name和location 但代值一定要代完整
		print "来自%s的鱼%s开始跳起来了。 "%(self.location,self.name)#后面不要漏了% 忘记缩进  如果name没写self 不能运行


def main():
	allen=Fish("allen","shanghai")   #  =的形式，调用了上面init的函数，  =类

	allen.jump() #调用jump的代码块 中间是. 后面忘加()


if __name__ == '__main__':
	main()

	# 总结：
	# 1.类是现实物质体的对应体，把常见的功能描述清楚。
	# eg.要描述大部分的鱼，假设大部分鱼都能跳，我的鱼就有跳的方法
	# 	假设这些鱼都有名字，产地，就能定制出自己的鱼

	# 	也可以自己定义一个turtle


class Dog():
	def __init__(self, name,location):
		self.name = name
		self.location=location

	def shout(self):  #忘记写self
		print "%s的%s大半夜的一直在叫。 "%(self.location,self.name)

	def stop(self):
		print "我泼了一桶水下去，%s收到惊吓，就不敢再惹姑奶奶我了。"%(self.name)



def main():
	hotdog=Dog('hotdog',"楼下")
	hotdog.shout()
	hotdog.stop()

if __name__ == '__main__':
	main()


class Cat():
	def __init__(self, name,location): #注意这里不要写成self.name,self.location
		
		self.name = name
		self.location=location

	def sing(self):
		print '%s的%s听到音乐唱起了歌。 '%(self.location,self.name)


def main():
	miaomiao=Cat('miaomiao','歌舞厅')
	miaomiao.sing()

if __name__ == '__main__':
	main()