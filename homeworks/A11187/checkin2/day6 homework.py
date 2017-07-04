#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xiangrikui
# 1. 老妈来到了菜市场
def print_list(lst):
	for lst_item in lst:  #遍历
		print 'mother sees %s '% (lst)

def buyornot(index):
	if index%2 == 0:
		return True
	else:
		return False

def main():
	print 'mother comes to the market'
	lst = ['cabbage','carrot','tomato','turtle','shrimp','sheng jiang','bai shao','xi you','beef','dumpling']
	index = 0
	amount = 0
	buy = False

	for lst_item in lst:
		if buyornot(index):
			amount = index + 1
			print 'mother sees %s, and buy %d kilos' % (lst[index], amount)
		else:
			print 'mother sees %s, and she does not buy it' % (lst[index])
		index = index + 1

		if index < 10:
			print 'mother continues her shopping'
		else:
			print 'mother goes back home'

if __name__ == '__main__':
	main()
#  2. 完成后，用今天的学到的列表知识，加 3 个菜
def main():
	print '..........'
	lst = ['cabbage','carrot','tomato','turtle','shrimp','sheng jiang','bai shao','xi you','beef','dumpling']
	lst.append('cucumber')
	lst.append('eggplant')
	lst.append('potato')
	print_list(lst)
if __name__ == '__main__':
	main()

#  3
def main():
	print '.....'
	lst = ['cabbage','carrot','tomato','turtle','shrimp','sheng jiang','bai shao','xi you','beef','dumpling']
	lst2 = lst[5:10]
	for lst_item in lst2:
		print lst2
	
if __name__ == '__main__':
	main()