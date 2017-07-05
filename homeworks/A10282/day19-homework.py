#!/usr/bin/python
# -*- coding: utf-8 -*
# @author: 233


class Dog():
  def __init__(self, name, location):
    self.name = name
    self.location = location

  def run(self):
    print '一到 %s 的狗 %s 开始跑起来了' %(self.location, self.name)
def main():
  
  brown = Dog('brown', '公园')
  brown.run()

if __name__ == '__main__':
  main()