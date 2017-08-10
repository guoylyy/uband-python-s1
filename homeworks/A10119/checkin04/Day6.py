#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Xiangwan

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



  	  
def homework():
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
	#心痛，这一部分做了几个小时！我一直陷在蜀黍给的sample里面，认为需要在append后面加上函数名称，
	#以指向到底是哪个代码块里面要加上这几个内容，其实单纯添加到列表里面的话，不需要那么复杂，直接在下面添加就可以了。
	lst.append('茄子')
	lst.append('土豆')
	lst.append('豆角')
	print '老妈来到菜市场 '
	index = 0

	for index, lst_item in enumerate(lst):
		if index % 2 == 0:
			print '老妈看到 %s , 买了 %d 斤 ' % (lst_item, index+1)
			if (index + 1) == 13:
				print '好啦，老妈心满意足地回家了 '
			else:
				print '老妈继续逛 '
		else:
			print '老妈看到%s, 不买' % (lst_item)
			if (index + 1) == 13:
				print '好啦，老妈心满意足地回家了 '
			else:
				print '老妈继续逛 '


	print '-------'


def print_list2(lst2):
	for lst2_item in lst2:#遍历
		print '老妈看到了%s '% (lst2_item)
def main2():
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']

	lst2 = lst[4:9]
	print_list2(lst2)


if __name__ == '__main__':
	homework()
	main2()