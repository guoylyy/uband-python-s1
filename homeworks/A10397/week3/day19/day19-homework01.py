#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tangxiaocu

class Cat():
  def __init__(self, name, location):
    self.name = name
    self.location = location

  def meow(self):
    print '来自 %s 的猫 %s 喵喵叫起来' %(self.location, self.name)

def main():

  Sonja = Cat('Sonja', 'Norway')
  Sonja.meow()




if __name__ == '__main__':
	main()