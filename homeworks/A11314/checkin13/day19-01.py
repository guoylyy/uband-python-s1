#!usr/bin/python
#coding:utf-8

class panda():
	"趴趴熊"
	pandacount=0
	foodcount = 0
	def __init__(self,name,bamboo=0):
		self.name = name
		self.bamboo = bamboo
		panda.pandacount += 1
		panda.foodcount = panda.foodcount + bamboo
	def climd(self):
		print "%s 趴趴……" % self.name
	def food(self):
		print "吃了 %d 个……" % self.bamboo



def main():
	papa1 = panda("缓缓",20)
	papa2 = panda("源源",19)
	papa1.climd()
	papa1.age = 3
	papa2.age = 10
	print "现在有%d个熊猫，他们吃了%d个竹子" %(panda.pandacount,panda.foodcount)
	print hasattr(panda,"food")
	print hasattr(panda,'age')
	print hasattr(panda,'mv')

if __name__ == '__main__':
	main()