#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Anqi
def first_step():
	lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺'] 
	print '老妈来到菜市场'
	return lst

def print_list(lst):
	index=0
	for index,lst_item in enumerate(lst):
		if index%2 == 0:
			print '老妈看到%s，买了%d斤，老妈继续逛' % (lst_item, index+1)
		else:
			print '老妈看到%s，不买，老妈继续逛'% (lst_item)

def main():
	lst = first_step()
	print_list(lst) 
if __name__ == '__main__':
  main()