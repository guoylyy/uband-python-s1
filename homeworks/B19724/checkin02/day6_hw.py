#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY

def main():
	print '老妈来到菜市场'
	lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	#index =  0 index这个指数是默认为0的
	for index,lst_item in enumerate(lst):
		if index % 2 == 0:
			buy_amount = index + 1
			print '老妈看到了 %s，买了 %d 斤' % (lst_item, buy_amount)
			print '老妈继续逛'
		else:
			print '老妈看到了 %s，不买' % (lst_item)
			print '老妈继续逛'
	print '---------'
	
	lst.append('猪肉')
	lst.append('鸡蛋')
	lst.append('茄子')#要分开添加
	
	print_list(lst)
	print '----------'

	lst2 = lst[4:10] #中间用冒号
	print_list(lst2)

def print_list(lst):
	for lst_item in lst:
		print '老妈看到了 %s ' % (lst_item)

if __name__ == '__main__':
	main()