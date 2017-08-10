#!/usr/bin/python
# -*- coding: utf-8 -*
 
class Bird():
  def __init__(self, name, location):
    self.name = name
    self.location = location
 
  def fly(self):
    print '来自 %s 的鸟 %s 开始飞起来了' %(self.name, self.location)
 
 
class Bird():
  def __init__(self, name):
    self.name = name
 
  def fly(self, height):
    print '%s 飞了 %d 米' %(self.name, height)
 
  def down(self):
    print '%s 摔死了' %(self.name)
 
 
def main():
  # angile = Bird('angile')
  # angile.fly(800)
  # angile.down()
  allen = Bird('allen', 'shanghai')
  allen.fly()
 
if __name__ == '__main__':
  main()