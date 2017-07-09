#!/usr/bin/python
# -*- coding: utf-8 -*
#Author: Pennsylvania

class Dog():

  def __init__(self, name, location):
    self.name = name
    self.location = location

  def bark(self):
    print '来自 %s 的狗 %s 开始叫起来了' % (self.location, self.name)

  def run(self):
  	print '原来是 %s 看到了它讨厌的猫' % (self.name)


def main():
  Athena = Dog('Athena', 'Urumqi')
  Athena.bark()
  Athena.run()





if __name__ == '__main__':
  main()