#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

def main():
	print '老妈来到菜市场'
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
	index = 0
	for lst_item in lst:
		if index % 2 == 0:
			print '老妈看到了 %s, 买了 %d 斤'% (lst_item, index + 1)
		else:
			print '老妈看到了 %s, 没买'% (lst_item)
		index = index + 1
		print '老妈继续逛'

	print '----'
	lst.append('毛肚')
	lst.append('土豆')
	lst.append('生菜')
	length = len(lst)

	lst2 = lst[5:10]

	index = 0
	print lst2
	for lst_item in lst2:
		if index % 2 == 0:
			print '老妈看到了 %s, 买了 %d 斤'% (lst_item, index + 1)
		else:
			print '老妈看到了 %s, 没买'% (lst_item)
		index = index + 1
		print '老妈继续逛'



if __name__ == '__main__':
	main()

