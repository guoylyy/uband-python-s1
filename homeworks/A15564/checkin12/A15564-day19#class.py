#!/usr/bin/python
# -*- coding: utf-8 -*
# @author: shangxindepidan

class Kid():
  def __init__(self, name, gender, age):
    self.name = name
    self.gender = gender
    self.age = age

  def intro(self):
    if self.gender == 'boy':
      print 'This is %s, he is %d years old.' %(self.name, self.age)
    else:
      print 'This is %s, she is %d years old.' %(self.name, self.age)

  def SetName(self, name):
    self.name = name

  def reintro(self):
    if self.gender == 'boy':
      print "Now he changes his name into '%s'." %(self.name)
    else:
      print "Now she changes her name into '%s'." %(self.name)

def main():
  Jack = Kid('Jack', 'boy', 8)
  Jack.intro()
  Jack.SetName('Jackie')
  Jack.reintro()

  Lily = Kid('Lily', 'girl', 7)
  Lily.intro()
  Lily.SetName('Lilian')
  Lily.reintro()


if __name__ == '__main__':
  main()
  