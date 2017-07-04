#!/usr/bin/python
# -*- coding: utf-8 -*-
# author=小八

class Car():
  def __init__(self, brand, speed):
    self.brand = brand
    self.speed = speed

  def be_drived(self, distance):
    hour = float(distance)/self.speed
    print '驾驶 %s 开 %dkm 去b地开了 %0.2f 小时' % (self.brand,
       distance, hour)

def main():
  car1 = Car('捷达',60)
  car1.be_drived(300)

  car2 = Car('捷豹', 120)
  car2.be_drived(400)

  
if __name__ == '__main__':
  main()
