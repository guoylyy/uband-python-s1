#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tangxiaocu
def print_list(lst):
	for lst_item in lst: #遍历
		print '老妈看到了%s' % (lst_item)

def main():
	#       0          1          2       3        4
	lst = ['大白菜 ', '空心菜', '花菜', '生姜 ', '小龙虾' ] #列表

	# 循环访问
	for lst_item in lst: #遍历
		# print '老妈看到了 %s ' % (lst_item)
		pass

	# 迭代访问
	for index,lst_item in enumerate(lst):
		# print '老妈看到了 %s ' % (lst_item)
		# print '当前第 %d 个' %(index)
		pass

	# 记录下标
	index = 0
	for lst_item in lst: #遍历
		# print '老妈看到了 %s' % (lst_item)
		# print '当前第 %d 个' % (index)
		index = index + 1

	#取值
	print lst[0]
	print lst[4]
	print '-----'

	#长度 【即为列表项数和】
	print len(lst)
	print '---'

	#加
	lst.append('白芍')
	print_list(lst)

	#删除
	del lst[0]
	print '----'
	print_list(lst) 

	#切片
	lst2 = lst[2:5] # 2,3,4
	print "------"
	print_list(lst2)


if __name__ == '__main__':
	main()