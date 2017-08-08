#!/usr/bin/python
# -*- coding: utf-8 -*

class Fish():
  def __init__(self, name, location):
    self.name = name
    self.location = location

  def jump(self):
    print ' 来自 %s 的鱼 %s 开始跳起来了 ' %(self.location, self.name)


class Rabit():
  def __init__(self, name,location):
    self.name = name
    self.location=location
    

  def jump(self):
    print ' 来自%s的名叫%s兔子跳了起来，被抓住然后吃掉了 ' %(self.location,self.name,)




def main():
  # angile = Bird('angile')
  # angile.fly(800)
  # angile.down()
  Stupid = Rabit('Stupid','shanghai')
  Stupid.jump()

if __name__ == '__main__':
  main()