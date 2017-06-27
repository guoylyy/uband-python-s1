#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu
cusine_list = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
def buybuybuy():
	index = 0
	buy_amout = 0
  	print '老妈来到了菜市场'
	for food in cusine_list:
		if index % 2 == 0:
			buy_amout = index + 1
			print '老妈看到了%s, 买了%d斤' % (food,buy_amout)
		else:
			print '老妈看到了%s,不买' % (food)
			print '老妈继续逛'
		index = index +1
def add_buy():
	cusine_list.extend(['皮皮虾','帝王蟹','牛蛙'])
	print '---------'
	for food in cusine_list:
		print food
def less_buy():
	#0白菜,'1萝卜','2西红柿','3甲鱼','4龙虾','5生姜','6白芍','7西柚','8牛肉','9水饺','10皮皮虾'，'11帝王蟹','12牛蛙'
	cusine_list2 = cusine_list[4:9]
	index = 0
	buy_amount = 0
	print '-------------'
	for food in cusine_list2:
		if index % 2 == 0:
			buy_amount = index + 1
			print '老妈看到了%s, 买了%d斤 ' % (food,buy_amount)	
		else:
			print '老妈看到了%s, 没有买 ' % (food)
		index = index + 1

if __name__ == '__main__':
	buybuybuy()
	add_buy()
	less_buy()
