#!/usr/bin/python
# -*- coding: utf-8 -*

class Cat():
  def __init__(self,name,color):
    self.name = name
    self.color = color

  def scratch(self,time):
    print '%s 的 %s 挠了 %d 次' %(self.color,self.name,time)

class Dog():
  def __init__(self,name):
    self.name = name

  def bark(self,time):
    print '%s 叫了 %d 声' %(self.name,time)


def main():
  kitty = Cat('kitty','白色')  
  kitty.scratch(3)
  puppy = Dog('puppy')
  puppy.bark(5)

if __name__ == '__main__':
  main()