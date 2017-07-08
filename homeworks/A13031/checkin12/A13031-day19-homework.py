#!/usr/bin/python
#	-*-	coding:	utf-8	-*-
#	@author:	xxx


class Singer():
	def __init__(self, name,location,location2):
		self.name=	name
		self.location=	location
		self.location2	=	location2

	def sing(self):
		print	'来自%s的%s唱了歌'	%(self.location,self.name)

	def songs(self,times):
		print	'%s总共唱了%d首歌'	%(self.name,times)

	def end(self):
		print	'%s在%s完美的结束了个人的表演'	%(self.name,self.location2)
			
def main():
	Brian	=	Singer('Brian','China','Tokyo')
	Brian.sing()		
	Brian.songs(15)
	Brian.end()


if __name__ == '__main__':
	main()