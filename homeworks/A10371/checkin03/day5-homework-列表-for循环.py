#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yuanzi

def main():
	
	lst = ['大白菜','花菜','空心菜','生姜','小龙虾']
	for lst_item in lst: 
	  print '老妈看到了 %s ' % (lst_item)
	print '~~~~~~~~~~~~~~~'

def main2():
	my_food_list = ['牛奶','饼干','薯片','海苔','虾条','可乐']
	print '我要买', len(my_food_list), '种零食，它们是'
	for item in my_food_list:
		print '%s' % (item)

if __name__ == '__main__':
	main()
	main2()

#list 是一个数据结构，把所有的项目都有序的放在一个列表里，就像一个清单一样
#for ... in 循环在列表中各项目间递归，把list里的项目一个个列出来
#递归就是程序调用自身的编程技巧