#!/usr/bin/python
# -*- coding: utf-8 -*-


def main1():
	dog1='大狗meimei'
	amount1=3
	minute=5
	print '小明到家， %s 奔向他，小明给了他 %d 根火腿， %s 花了 %d 分钟吃完了'

	dog2='小狗huahua'
	amount2=1
	minute=6
	print '小明到家，%s 奔向他，小明给了他 %d 根火腿， %s 花了 %d 分钟吃完了'


class dog():
	def __init__(self, name, amount, times):

		self.name = name
		self.amount = amount
		self.times = times


	def eat(self):
		print '小明回家，%s 奔向他， 小明给了 %s %d 根火腿， %s 花了 %d 分钟吃完了' %(self.name, self.name, self.amount, self.name, self.times)

def main2():
	dog1= dog('大狗meimei',3,5)
	dog1.eat()

	dog2= dog('小狗huahua',1,6)
	dog2.eat()



if __name__ == '__main__':
	main2()
