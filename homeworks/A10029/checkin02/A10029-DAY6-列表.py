#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:  zi le

# 今日的作业
# 有十种菜
#   白菜、萝卜、西红柿、甲鱼、龙虾、生姜、白芍、西柚、牛肉、水饺
# 
# 1. 老妈来到了菜市场，从下标 0 开始买菜，遇到偶数的下标就买
#    遇到奇数的下标就不买，买的数量为下标 + 1 斤
#    （请写程序模拟整个过程）
#    （注意单一职责原则）
#    （注意灵活使用 def 函数（代码块））
#    
# 【提示】：
#   输出结果可能为
#   ‘老妈来到菜市场
#    老妈看到白菜，买了 1 斤
#    老妈继续逛
#    老妈看到xxx, 不买
#    老妈继续逛
#    ...
#   '
#  2. 完成后，用今天的学到的列表知识，加 3 个菜
#  3. 完成后，用今天的学到的列表知识，让老妈只逛第 5~9 个菜
def list():
	#       0      1        2        3        4       5       6       7       8       9
	lst=['白菜 ','萝卜 ','西红柿 ','甲鱼 ','龙虾 ','生姜 ','白芍 ','西柚 ','牛肉 ','水饺 ']
	index=0
	print '老妈来到菜市场 '
	for lst_item in lst:
		number=index+1
		if index%2:
			print '老妈看到%s，买了 %d 斤， '%(lst_item,number)
			print '老妈继续逛 '
		else:
			print '老妈看到%s，不买， '%(lst_item)
			print '老妈继续逛 '
		index=index+1
	print '------------------------- '
	return lst

			

def add_list(lst):
	lst.append('韭菜 ')
	lst.append('黄瓜 ')
	lst.append('苦瓜 ')
	for lst_item in lst:
		print '%s'%(lst_item)

	
	print '------------------------- '		

def buy_list(lst):
	lst2=lst[5:10]
	index=5
	print '老妈来到菜市场 '
	for lst_item in lst2:
		number=index+1
		if index%2:
			print '老妈看到%s，买了 %d 斤， '%(lst_item,number)
			print '老妈继续逛 '
		else:
			print '老妈看到%s，不买， '%(lst_item)
			print '老妈继续逛 '
		index=index+1



def	main():
	lst=list()
	add_list(lst)
	buy_list(lst)


if __name__ == '__main__':
  main()