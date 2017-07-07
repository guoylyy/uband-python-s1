#!/usr/bin/python
# -*- coding: utf-8 -*

class Fish():
  def __init__(self, name, location):
    self.name = name
    self.location = location

  def jump(self):
    print '来自 %s 的鱼 %s 开始跳起来了' %(self.location, self.name)


class Bird():
  def __init__(self, name):
    self.name = name

  def fly(self, height):
    print '%s 飞了 %d 米' %(self.name, height)

  def down(self):
    print '%s 摔死了' %(self.name)

class Dog():
  def __init__(self,name):
    self.name = name
  def bark(self):
    print 'The dog %s is barking' % self.name
  def meat(self):
    print 'The dog %s is eating meat.' % self.name
def main():
  # angile = Bird('angile')
  # angile.fly(800)
  # angile.down()
  # allen = Fish('allen', 'shanghai')
  # allen.jump()
  TianTian = Dog('TianTian')
  TianTian.bark()
  TianTian.meat()

if __name__ == '__main__':
  main()