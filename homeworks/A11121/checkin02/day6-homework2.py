#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Jinxiao

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

def buybuybuy(lst2):
	
	index = 0
	#for lst_item in lst:
	#	print '老妈看到了 %s' %(lst_item)
	#	print '老妈看到第%d个'%(index)
	#	index = index + 1

	for index, lst_item in enumerate(lst2):
		if index%2:
			print '老妈看到了第%d个菜，是%s，不买' %(index, lst_item)
		else:
			print '老妈看到了第%d个菜，是%s，买了%d个' %(index, lst_item, index+1)
		
		index = index + 1

def goods():
	
	print '小金人的老妈来到菜市场。'
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
#  2. 完成后，用今天的学到的列表知识，加 3 个菜
	lst.append('豆腐') #只能一次加一个
	lst.append('豆苗')
	lst.append('鳝鱼')

	print '看到%d种菜'%len(lst)	
#  3. 完成后，用今天的学到的列表知识，让老妈只逛第 5~9 个菜
	lst = lst[5:10] #有疑问，这样子一来，index也变了，如何保留原来的index呢？不知道这样是否符合题意呢？


	return lst #注意！return也是语句之一，不要和def对齐，也要缩进！

def main():
	lst2 = goods()
	buybuybuy(lst2)





#def print_lst()
#if index%2:
#		print '老妈看到list'
	

if __name__ == '__main__':
		main()

