#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: younmpjlt

class Fish():
	def __init__(self, name, location):
		self.name = name 
		self.location = location
	def jump(self):
		print '来自%s的鱼%s跳起来了'%(self.location, self.name)




class Cat():
	def __init__(self, name, location,name2,name3):
		self.name = name
		self.location = location
		self.n2 = n2 #提米
		self.n3 = n3 #妈妈

	def smile(self):
		print '来自%s的猫%s笑了' %(self.location, self.name)

	def run(self,length):
		print '然后它跑了%d米' %(length)

	def bump_into_someone_else(self):
		print '可是%s撞到了%s' %(self.name,self.n2)
		
	def cry(self):
		print '然后%s就哭了起来，哭着去找%s' %(self.n2,self.n3)



def main():
	allen = Fish('allen','shanghai')
	allen.jump()

	Susu = Cat('Susu','Jiangsu','提米','妈妈')
	Susu.smile()
	Susu.run(4)
	Susu.bump_into_someone_else()
	Susu.cry()


if __name__ == '__main__':
	main()



	#来自shanghai的鱼allen跳起来了
    #来自Jiangsu的猫Susu笑了
    #然后它跑了4米
    #可是Susu撞到了提米
    #然后提米就哭了起来，哭着去找妈妈	

    