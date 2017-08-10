#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yan


lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']

def shop(lst):
	print '老妈来到菜市场'
	for index,lst_item in enumerate(lst):
		if index % 2 == 0:
			amount = index+1
			print '老妈看到了%s，买了%d斤' %(lst_item, amount)
		else:
			print '老妈看到了%s，不买' %(lst_item)
		print '老妈继续逛'
		index =index+1
	print '-----------------'

#2加菜
lst_more = lst[:]
lst_more.append('土豆')
lst_more.append('西兰花')
lst_more.append('鸡肉')


#3只逛5~9个菜
lst_less = lst[5:10]


if __name__ == '__main__':
	shop(lst)
	shop(lst_more)
	shop(lst_less)