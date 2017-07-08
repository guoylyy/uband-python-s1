# -*- coding: utf-8 -*-
# @author: shuan
class pen():
	def __init__(self, name):
	    self.name = name
	   

	def write(self,color):
	    self.color = color	
	    print '%s可以写出%s的字'%(self.name, self.color)

	def broken(self):
		print '%s坏了'%(self.name)

def main():
	ballpen = pen('ballpen')
	ballpen.write('red')
	ballpen.broken()


if __name__ == '__main__':
 main()