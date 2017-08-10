#coding=utf_8
class Cat():
	def __init__(self,name,color):
		self.name=name
		self.color=color
	def run(self,distance):
		print '%s色的小猫%s跑了%d米 '%(self.color,self.name,distance)
	def eat(self,fishname,amount):
		print '%s色的小猫%s吃了%d条%s'%(self.color,self.name,amount,fishname)
	def play(self,item):
		print '%s色的小猫%s在玩%s'%(self.color,self.name,item)
def main():
	Kitty=Cat('Kitty','white')
	Kitty.run(10)
	Kitty.eat('金枪鱼',2)
	Kitty.play('线球')
if __name__ == '__main__':
	main()

	