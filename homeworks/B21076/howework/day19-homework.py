#!/usr/bin/python
# -*- coding: utf-8 -*
class Person():
  def __init__(self, name, country):
    self.name = name
    self.country = country

  def sayHello(self):
        print 'Hello,I am %s and I come from %s!'%(self.name,self.country)
  def sayGoodBye(self):
        print 'GoodBye,%s'%(self.name)


def main():
	chinese=Person('zhangsan','China')
	chinese.sayHello()
	chinese.sayGoodBye()
	american=Person('Mansur','America')
	american.sayHello()
	american.sayGoodBye()


if __name__ == '__main__':
  main()