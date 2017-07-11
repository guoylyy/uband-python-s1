#!/usr/bin/python
# -*- coding: utf-8 -*

class Lipstick():
  def __init__(self, color_number, brand):
    self.color_number = color_number
    self.brand = brand
    

  def popular_color(self):
    print ' %s 的口红 %s 是热门款' %(self.color_number, self.brand)


class Cat():
  def __init__(self, name):
    self.name = name

  def jump(self, height):
    print '%s 跳了 %d 个高儿' %(self.name, height)

  def meow(self):
    print '%s 喵了一声' %(self.name)


def main():
 
  Chanel = Lipstick('Chanel', 'No.43')
  Chanel.popular_color()

  Monkey = Cat('Monkey')
  Monkey.jump(3)
  Monkey.meow()

if __name__ == '__main__':
  main()