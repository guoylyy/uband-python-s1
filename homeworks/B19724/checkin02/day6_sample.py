#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY

def main():
	#        0          1       2       3      4
	lst = ['大白菜', '空心菜','花菜','生姜','小龙虾']
	#循环访问
	for lst_item in lst: #遍历
		print '老妈看到了 %s ' % (lst_item)
	print '--------------'
	
	#记录下标
	index = 0
	for lst_item in lst:
		print '老妈看到了 %s ' % (lst_item)
		print '当前第 %d 个' % (index)
		index = index + 1
	print '--------------'

	#迭代访问
	for index,lst_item in enumerate(lst):
		print '老妈看到了 %s ' % (lst_item)
		print '当前第 %d 个' % (index)
	print '------------'

	#取值
	print lst [0]
	print lst [4]
	print '-------'

	#长度
	print len(lst)

	#加
	lst.append('白芍') #不理解
	print_list(lst)
	print '-----'

	#删除
	del lst [0]
	print_list(lst)
	print '-----'

	#切片
	lst2 = lst [2:5] #前闭后开 区间[2,5) 2,3,4
	print_list(lst2)

def print_list(lst): #不理解
	for lst_item in lst:
		print '老妈看到了 %s '% (lst_item)


if __name__ == '__main__':
	main()