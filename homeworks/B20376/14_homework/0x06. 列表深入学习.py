#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Emma


def print_list(lst):
	for lst_item in lst:
		print '老妈来到了菜市场，看到了 %s ' %(lst_item)

def main():

	print '老妈来到了菜市场'
	
	lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	

	for index,lst_item in enumerate(lst):
		if index % 2 == 0:
			print '老妈看到了 %s ,老妈没有买,继续往前逛' %(lst_item)
		else:
			print '老妈看到了 %s ' %(lst_item)
			print '买了 %d 斤' %(index+1)


	lst.append('南瓜')
	lst.append('生菜')
	lst.append('羊肉')
	print_list(lst)


	lst2 = lst[4:9]
	for index2,lst_item2 in enumerate(lst2):
		if index % 2 == 0:
			print '老妈看到了 %s ,老妈没有买,继续往前逛' %(lst_item2)
		else:
			print '老妈看到了 %s ' %(lst_item2)
			print '买了 %d 斤' %(index2+1)


if __name__ == '__main__':
	main()