#!/usr/bin/python
# -*- coding: utf-8 -*
# @author: yuanzi
class Kids():
  def __init__(self, name):
  	self.name = name

  def eat(self, number):
  	print '%s 嘴馋,偷吃了%d根冰棍' %(self.name, number)

  def drink(self, cup):
  	print '%s 又喝了%d 杯冰可乐' %(self.name, cup)

  def sick(self):
  	print '%s 吃太多凉的食物,肚子好难受啊' %(self.name)

  def cure(self):
  	print '%s喝了热水之后好多了,下次再也不能贪吃了' %(self.name)

def main():
  micky = Kids('micky')
  sam = Kids('sam')
  micky.eat(5);micky.drink(3);micky.sick()
  micky.cure()
  sam.eat(7);sam.sick();sam.cure()
		

if __name__ == '__main__':
  	main()  
