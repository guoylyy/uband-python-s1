# -*- coding: utf-8 -*-

class activity():
  def __init__(self, vehicle, day, hour):
  	self.vehicle= vehicle
  	self.day = day
  	self.hour = hour

  def speed (self,distance):
    speed = float(distance) / self.hour
    print ('%s 老妈骑了 %s 去买菜，平均速度是 %g' % (self.day, self.vehicle, speed))

def main():
    activity1 = activity('电动车', '周一', 0.5)
    activity1.speed(20)

    activity2 = activity('自行车', '周二', 2)
    activity2.speed(20)

    activity3 = activity('电动车', '周三', 0.6)
    activity3.speed(20)

if __name__ == '__main__':
	main()

