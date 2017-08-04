#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Anna




def main():
	      #  1       2        3        4      5       6      7       8       9      10       
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
	lst.append('菠萝')
	lst.append('羊肉')
	lst.append('黄瓜')
	for index,lst_item in enumerate(lst):
		buy_amount = index + 1 
		num = index
		if num%2 == 0:
			print '老妈看到了 %s, 买了 %d 斤' % (lst_item, buy_amount)
		else:
			print '老妈看到了 %s, 不买' % (lst_item)
	
	
	
def main2():
	      #  0       1        2        3      4       5     6       7       8      9       
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
	
	lst2 = lst[4:9]
	for lst2_item in lst2:
		print "老妈今天只逛了 %s " % (lst2_item)


if __name__ == '__main__':
	main()
	main2()