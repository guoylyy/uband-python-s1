#!/usr/bin/python
# -*- coding: utf-8 -*

class Cat():
  def __init__(self, name, location):
    self.name = name
    self.location = location

  def run(self):
    print '来自 %s 的猫 %s 跑了过来' %(self.location, self.name)  

  def jump(self):
    print '来自 %s 的猫 %s 跳了起来' %(self.location, self.name)



def main():

  Tom = Cat('Tom', 'USA')
  Tom.jump()
  Tom.run()

if __name__ == '__main__':
  main()