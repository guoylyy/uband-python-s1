#!/usr/bin/python
# -*- coding: utf-8 -*



class Door():
  def __init__(self, name):
    self.name = name

  def open(self, someone):
    print '%s 被 %s 打开了' %(self.name, someone)

  def close(self, someone):
    print '%s 被 %s 关上了' %(self.name, someone)


def main():
  door_of_study = Door('door_of_study')
  door_of_study.open('Lucy')
  door_of_study.close('Lily')

if __name__ == '__main__':
  main()