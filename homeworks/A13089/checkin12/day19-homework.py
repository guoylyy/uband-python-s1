#!/usr/bin/python
# -*- coding: utf-8 -*
# @author: pluto

class Cat():
	def __init__(self,name):
		self.name = name
		
	def catch_mice(self,mouse_name):
		print '%s猫捉住了%s鼠 '%(self.name,mouse_name)

	def bite_people(self,time):
		print '%s又咬了主人%d次 '%(self.name,time)


def main():

  Tom=Cat('Tom')
  Tom.catch_mice('Jerry')
  Tom.bite_people(1)

if __name__ == '__main__':
  main()