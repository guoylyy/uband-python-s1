#!/usr/bin/python
# -*- coding: utf-8 -*-

class transport():
  def __init__(self, day, vehicle):
    self.day = day
    self.vehicle = vehicle
  def drive(self,hour):
    speed = distance / hour
    print '老妈在%s骑%s平均时速为%0.2f km/h' %(self.day, self.vehicle, speed)


def main():
  distance = 20
  day1 = transport('周一','电动车')
  day2 = transport('周二','自行车')
  day3 = transport('周三','电动车')

  day1.drive = (0.5)
  day2.drive = (2)
  day3.drive = (0.6)

  

if __name__ == '__main__':
  main()
