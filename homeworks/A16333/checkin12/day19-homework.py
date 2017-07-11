#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: chendasuan

class cat():
  def __init__(self,name,location,age):
  	self.name = name
  	self.location = location
  	self.age = age
  def eat(self):
    print '%d 月大的%s猫咪%s 喜欢吃鱼  ' % (self.age, self.location, self.name)
  def what_it_eat(self):
    if self.age  < 6 :
      print '%d 月大的%s 猫咪%s 喝牛奶 ' % (self.age, self.location, self.name)
    if self.age >= 6 :
      print '%d 月大的%s 猫咪%s 吃猫粮 ' % (self.age, self.location, self.name)
  def whose(self):
  	print 'Hello Kitty 是我家的猫 '

def main():
  Hello_Kitty = cat('Hello_Kitty','Japan',12)
  Hello_Kitty.eat()
  Hello_Kitty.what_it_eat()
  Hello_Kitty.whose()

if __name__ == '__main__':
  main()





  	

