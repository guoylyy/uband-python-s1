#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: caramel

def print_list(lst):
	for lst_item in lst:
		print '老妈看到了 %s ' % (lst_item)

def main():
    #        0          1       2       3       4
	lst = ['大白菜', '空心菜', '花菜', '生姜', '小龙虾']
	#循环访问
	#for lst_item in lst:  #遍历
	#	print '老妈看到了 %s ' % (lst_item)
	pass

#记录下标
	index = 0
	for lst_item in lst:
	#	print '老妈看到了 %s ' % (lst_item)
	#	print '当前第 %d个' % (index)
		index = index + 1

#迭代访问
	for index, lst_item in enumerate(lst):
	#	print '老妈看到了 %s ' % (lst_item)
	#	print '当前第 %d 个' % (index)
		pass


#取值
	print lst[2]

#长度
	print len(lst)

#加
	lst.append('猪肉')
	print_list(lst)
#删除
#	del lst[2]
	print '-------'
#	print_list(lst)

#切片
	lst2 = lst[0:3]  #左开右彼区间,区第二个到第四个记为[2:5]
	print_list(lst2)

if __name__ == '__main__':
  main()