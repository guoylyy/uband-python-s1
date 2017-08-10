#!/usr/bin/python
# -*- coding: utf-8 -*-
# ashley


  
class Flower():
  def __init__(self, name, location):
    self.name = name
    self.location = location
  def bloom(self):
    print ' 来自 %s 的玫瑰 %s 盛开了 ' %(self.location, self.name)
class animal():
  def __init__(self, name):
    self.name = name
  def fly(self,height):
    print '%s 飞了 %d 米这么高' %(self.name, height)

  def down(self):
    print ' %s 摔死了 ' %(self.name)

def main():

  you = Flower('rose', 'america')
  you.bloom()






if __name__ == '__main__':
  main()
