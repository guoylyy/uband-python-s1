#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Xiangwan


def homework():
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
	print '老妈来到菜市场 '
	index = 0

	for index, lst_item in enumerate(lst):
		if index % 2 == 0:
			print '老妈看到 %s , 买了 %d 斤 ' % (lst_item, index+1)
			if (index + 1) == 13:
				print '好啦，老妈心满意足地回家了 '
			else:
				print '老妈继续逛 '
		else:
			print '老妈看到%s, 不买' % (lst_item)
			if (index + 1) == 13:
				print '好啦，老妈心满意足地回家了 '
			else:
				print '老妈继续逛 '
	lst.append('茄子')
	lst.append('土豆')
	lst.append('豆角')
	homework()
	try: #感觉似乎，并没有把异常值处理好.........
		homework()
	except Exception,e:
		print '发生错误 %s' % (e)  
	else:
		print '没有异常 '
	print '-------'

def print_list2(lst2):
	for lst2_item in lst2:#遍历
		print '老妈看到了%s '% (lst2_item)
def main2():
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']

	lst2 = lst[4:9]
	print_list2(lst2)
if __name__ == '__main__':
	homework()
	main2()