#!/usr/bin/python
# -*- coding: utf-8 -*-


class Boy():

  def __init__(self, name):
    self.name = name
    

  def play(self, distance):
    self.distance = distance
    print ' %s 跑了%d 米,为马拉松做准备' % (self.name, self.distance)

  def time(self, minute):
    self.minute = minute
    print '%s 跑了 %d分钟后'% (self.name, self.minute)

  def relax(self):
    print '%s 跑累了，要休息休息'%(self.name)

def main():
  xiaoming = Boy('小明')
  xiaoming.play(10000)
  xiaoming.time(100)
  xiaoming.relax()



if __name__ == '__main__':
  main()
