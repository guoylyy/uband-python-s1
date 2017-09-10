#-*- coding:utf8 -*-

class Fish():
	"""docstring for Fish"""
	def __init__(self,name,location): #初始化一系列变量
		self.name=name
		self.location=location
	def jump(self):
		print "来自%s的鱼%s开始跳起来了"%(self.location,self.name)
class  Bird():
	"""docstring for  Bird"""
	def __init__(self, name):
		self.name=name

	def fly(self,height):
		print "%s飞了%s米"%(self.name,height)
	def down(self):
		print "%s停下来休息"%(self.name)

class Cat():
	"""docstring for Cat"""
	def __init__(self,name):
		self.name = name
	def play(self,runto,jumpto):
		print "%s跑到%s前面"%(self.name,runto)
		print "%s跳上了%s"%(self.name,jumpto)
	def sleep(self,hours):
		print "%s睡了%d小时"%(self.name,hours)	

def main():
	allen=Fish("allen","大海") #括号里比前面初始化时候括号里定义的少一个，不用定义self
	allen.jump() #jump的定义里只有self，这里就不用赋值
	barry=Bird("barry")#初始化定义了self，name，这里只用给name赋值
	barry.fly("50")#fly的定义里除了self之外还有height，这里要给height赋值
	barry.down()
	cat1=Cat("Hal")
	cat1.play("沙发","茶几")
	cat1.sleep(8)


if __name__ == '__main__':
	main()