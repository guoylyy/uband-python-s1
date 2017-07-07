#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Winnie

def print_list(lst):
  for lst_item in lst: 
    print '老妈看到了 %s '% (lst_item)

def main():
	print '老妈来到菜市场'
	
   
def main2():
	# homework1
	lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	
 
	for index,lst_item in enumerate(lst):
		if index % 2 == 0:
			print '老妈看到 %s, 买了 %d 斤' %(lst_item, index + 1)
			print '老妈继续逛'
		else:
			print '老妈看到 %s, 老妈不买' %(lst_item)
			print '老妈继续逛'


def main3():
	print '----------'
	#homework2
	lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	lst.append('鱼丸')
	lst.append('粗面')
	lst.append('云吞')
	print_list(lst)
	try: 
		print_list(ls)
	except e:
		print '发生错误：%s' %(e)

 


def main4():
	print '----------'
	#homework3
	lst = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
	lst2 = lst[5:10]
	print_list(lst2)

   


if __name__ == '__main__':
	main()
	main2()
	main3()
	main4()

  




