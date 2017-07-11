#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tingting

def print_list():
	print '老妈来到菜市场'
	for lst_item in lst:
		print '菜市场有%s' % (lst_item)

	print '---'

def main():	
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
	for index,lst_item in enumerate(lst):
		print '老妈看到了%s' % (lst_item)
		buy_amount = index + 1
		if (index % 2) == 0:
			print '买了%d斤' % (buy_amount)
			print '老妈继续逛'
		else:
			print '不买'
			print '老妈继续逛'

	print '---'

	lst.append('大蒜')
	print lst[10]
	lst.append('猪肉')
	print lst[11]
	lst.append('小葱')
	print lst[12]

	print '---'

	lst2 = lst[5:10]
	print_list(lst2)

if __name__ == '__main__':
	main()