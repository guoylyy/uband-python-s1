#!/usr/bin/python
# -*- coding: utf-8 -*
#author:sanlianyin


class cat():
  def __init__(self, name, location):
    self.name = name
    self.location = location

  def  pur(self):
    print '来自于 %s的猫 %s 叫起来了' % (self.location, self.name)
  def run(self):
  	print '%s 跑起来没人追的上' % (self.name)
  	
def main():
  Judy = cat('Judy', 'China')
  Judy.pur()
  Judy.run()


if __name__ == '__main__':
  main()