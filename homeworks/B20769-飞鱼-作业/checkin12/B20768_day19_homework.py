#!/usr/bin/python
# -*- coding: utf-8 -*
# @author: feiyu
#定义一个类

class Dog():
	def __init__(self, name, location, variety):
		self.name = name
		self.location = location 
		self.variety = variety
	def introduction(self):
		print '%s 是一只来自 %s 的 %s ' % (self.name, self.location, self.variety)	
	def jump(self):
		print '%s 跳了起来迎接它的“小伙伴”' % (self.name)
	def lick(self):
		print '%s 舔了舔它的“小伙伴”' % (self.name)
	def run(self, distance):
		self.distance = distance
		print '%s 跑了 %d 米去迎接它的“小伙伴”' % (self.name, self.distance)
	def circle(self):
		print '%s 围着它的“小伙伴”转圈 ' % (self.name)
	def see_off(self):
		print '%s 不舍的看着它的“小伙伴”出门' % (self.name)
		
class Kinder():
	def __init__(self, name):
		self.name = name
	def go_out(self):
		print '%s 出门了' % (self.name)
	def come_back(self):
		print '%s 回家了' % (self.name)
	def down(self):
		print '%s 蹲下来摸了摸它的“小伙伴”' % (self.name)

import time
def main():
 	xiaoming = Kinder('xiaoming')
 	jack = Dog('jack', 'Siberian', 'husky')
 	jack.introduction()
 	print '现在是：%s' %(time.strftime("%H:%M:%S", time.localtime()))
 	xiaoming.go_out()
 	jack.see_off()
 	print '1个小时以后'
 	xiaoming.come_back()
 	jack.run(200)
 	jack.circle()
 	xiaoming.down()
 	jack.lick()

if __name__ == '__main__':
  main()