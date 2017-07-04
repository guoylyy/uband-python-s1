#!/usr/bin/python
# -*- coding: utf-8 -*

class cat():
  def __init__(self, name):
    self.name = name
    print 'There is a cat called %s' % (self.name)

  def jump(self,height):
    print '%s 开始跳%.1f米 ' %(self.name, height)


  def run(self, length):
    print '%s 开始跑%.1f米 ' %(self.name, length)

  def bite(self):
    print '%s咬了人' %(self.name)
def main():
    Louise = cat ('Louise')
    Louise.jump(2)
    Louise.run(3)
    Louise.bite()

if __name__ == '__main__':
    main()