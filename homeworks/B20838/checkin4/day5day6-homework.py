#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: lightningLUO
def homework1():
	lst = ['叉烧包', '流沙包', '虾饺', '烧麦', '糯米鸡','马蹄糕' , '榴莲酥' , '肠粉', '龙井', '奶茶']
	print '老妈去吃早茶'

	index = 0
	for lst_item in lst:
		index = index +1


	amount = 0
	for lst_item in lst:
		if (index % 2) != 0:
			amount = index + 1
			print '老妈点了 %s, %d份' % (lst, amount)
		else:
			print '老妈看到了 %s,不点' % (lst)
		index = index + 1








def sample():
	#         0          1        2      3        4
	lst2 = ['大白菜', '空心菜', '花菜', '生姜', '小龙虾'] #列表
	#循环访问
	for lst2_item in lst2: #遍历
		print '老妈看到了 %s ' % (lst2_item)
		
	#记录下标
	print '--------------------'
	index = 0
	for lst2_item in lst2:
		print '老妈看到了 %s ' % (lst2_item)
		print '当前第%d 个' %(index)
		index = index + 1


	#迭代访问
	print '--------------------'
	for index,lst2_item in enumerate(lst2):
		print index
		print lst2_item

	#取值
	print '--------------------'
	print lst2[3]

	#长度
	print '---------------------'
	length = len(lst2)
	print '该列表有%d个元素 '%(length)

	#加
	lst2.append ('白芍')
	length = len(lst2)
	print '该列表有%d个元素 '%(length)

	#删除
	del lst2[0]
	for item in lst2: #遍历
		print item

	#切片
	lst3 = lst2[1:3]
	for item in lst3:
		print item

if __name__ == '__main__':
	homework1()
	sample()


