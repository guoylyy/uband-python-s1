#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tangxiaocu

#  2. 完成后，用今天的学到的列表知识，加 3 个菜
def main():


	lst = ['大白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
	lst.append('土豆')
	lst.append('玉米')
	lst.append('茄子')
	print '老妈来到菜市场 '

	for index,lst_item in enumerate(lst):
		if index% 2 == 0:
			print '看到了 %s，买了 %d 斤' % (lst_item, index + 1)
		else:
			print '看到了 %s，不买' % (lst_item)
		print '老妈继续逛'


if __name__ == '__main__':
	main()
	
