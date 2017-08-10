#!/usr/bin/python
# -*- coding: utf-8 -*-

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


# @author: B17455
def print_list(lst):
  for lst_item in lst:  #遍历
    #print '老妈看到了 %s '% (lst_item,)
    print lst_item,


def homework():
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉','水饺']
	index = 0

	print '我的老妈来到菜场买菜'

	for lst_item in lst:
		index = index +1
		if (index%2 != 0):
			print '老妈看到%s 买了%d斤'% (lst_item,index)

	print '------------'
	index = 0
	print '我的老妈在菜场继续逛,看到了：'
	for lst_item in lst:
		index = index +1
		if (index%2 == 0):
			#print '老妈看到%s 没有买'% (lst_item)
			print lst_item,
	print '\n但是没有买'

	print '------------'
	print '我的老妈在菜场继续逛，感觉要多看看3个菜，现在的菜单变成了：'

	#lst.append('大蒜')
	#lst2 = ['suan大蒜','da大葱', 'xi大西瓜']
	lst.append('大蒜')
	lst.append('大葱')
	lst.append('大西瓜')

	print_list(lst)
	print '\n总计有%d种菜'%len(lst)

	print '------------'
	lst0 = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
	lst3 = lst[5:10]
	print '我的老妈思来想去，只逛了几个菜，分别是：'
	print_list(lst3)

	index = 0

	for lst_item in lst3:
		index = index +1
		if (index%2 != 0):
			print '老妈看到%s 买了%d斤'% (lst_item,index)
		if (index%2 == 0):
			print '老妈看到%s 没有买'% (lst_item)


if __name__ == '__main__':
  homework()