#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tangxiaocu

def main():
	#         1         2         3       4        5
	lst = ['大白菜', '空心菜', '花菜', '生姜', '小龙虾'] #列表
	# 循环访问
	for lst_item in lst: #遍历
		print '老妈看到了 %s ' % (lst_item)

	# 记录下标
	index = 0
	for lst_item in lst: #遍历
		print '老妈看到了 %s ' % (lst_item)
		print '当前第 %d 个' % (index)
		index = index + 1

	# 迭代访问
	for index, lst_item in enumerate(lst):
		print '老妈看到了 %s ' % (lst_item)
		print '当前第 %d 个' % (index)


	#取值

	#长度

	#加

	#删除

	#切片

if __name__ == '__main__':
	main()