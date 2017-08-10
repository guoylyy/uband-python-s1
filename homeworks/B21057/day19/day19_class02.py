#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx
  
class Info(object):
  def __init__(self, phone, email, qq):
    self.phone = phone
    self.email = email
    self.qq = qq

    def get_phone(self):
      return self.phone

    def update_phone(self, newphone):
      self.phone = newphone
      print "手机号更改已更改"

    def get_email(self):
      return self.email

class Car():
	def __init__(self, brand, speed):
		self.brand = brand
		self.speed = speed

    
	def run(self,distance):

		hour = float(distance)/self.speed
		money = hour * 1 
		print("驾驶 %s 开 %d km 去b地开了 %0.2f 小时" %(self.brand,distance, hour))
		print("花费 %d 元" %(money))


def main():
  car1 = Car('摩拜',60) 

  car1.run(300)

  car2 = Car('小黄车',50) 
  car2.run(300)

  

if __name__ == '__main__':
	main()