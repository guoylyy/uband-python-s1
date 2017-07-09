#!/usr/bin/python
# -*- coding: utf-8 -*

class cat():
	def __init__ (self, name):#都有self这个属性，貌似是用来指代自己的 #initiate 的时候不用太多attribute， 免得自己后面不灵活
		self.name = name# init里面的要酱紫定义的意义是什么？ 可以在下面直接用，表示是class 的属性么
		
		
	def introduce (self, gender):
		print "喵主子%s初来乍到，是一只%s 猫 " % (self.name, gender)

	def bite (self,owner):
		print "喵主子 %s 不开森了，咬了铲屎官%s一口 "% (self.name, owner)

	def sleep (self,time):
		print "喵主子%s心满意足的睡了%d小时 " %(self.name,time)


def main():
	Charlotte = cat("鸭嘴兽")
	Charlotte.introduce("小公举")
	Charlotte.bite("heng")
	Charlotte.sleep(3)



		

if __name__ == '__main__':
  main()