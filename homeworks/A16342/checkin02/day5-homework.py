#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yan

def main2():
	goods = '大白菜，空心菜，花菜，生姜，小龙虾'
	print '老妈看到了%s'%(goods)  
	#pass

def main3():
	lst = ['大白菜','空心菜','花菜','生姜','小龙虾']
	print lst

	for lst_item in lst:
		print '老妈看到了 %s'%(lst_item)

	print '----------'
	#记录下标
	index = 0
	for  lst_item in lst:
		print '老妈看到了 %s' % (lst_item)
		print '当前第 %d 个' % (index)
		index = index +1
	
	print '----------'
	#迭代访问
	for index,lst_item in enumerate(lst):
		print '老妈看到了 %s' % (lst_item)
		print '当前第 %d 个' % (index)

	print '----------'
	#取值
	print lst[0]

	#长度
	print len(lst)

	#加
	lst.append ('白芍')

	#删除
	del lst[0]

	#切片
	lst2 = lst[2:5]

if __name__ == '__main__':
	main2()
	main3()
	