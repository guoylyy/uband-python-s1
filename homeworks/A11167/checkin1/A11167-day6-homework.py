#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

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
def print_list(lst):
  print '老妈来到菜市场，看到了 %s '% (lst)

def homework():
  print '老妈来到菜市场'
  lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
#作业1  
  for index, lst_item in enumerate(lst):
  	print '老妈看到 %s ' %(lst_item)
  	if index % 2 == 0: #遇到偶数的下标就买
  		print '花了 %d 元' %(index +1)
  else:
    print '不买，继续逛'

  print '---' #开始作业2
 
  lst.append('cabbage')
  lst.append('mushroom')
  lst.append('carrot')
  print_list(lst)

  print '---' #开始作业3
	
  lst2 = lst[4:9]
  for index2, lst_item2 in enumerate(lst2):
  	print '老妈看到 %s ' %(lst_item2)
  	if index2 % 2 == 0: #遇到偶数的下标就买
  		print '花了 %d 元' %(index2 +1)
	else:
		print '不买，继续逛'

if __name__ == '__main__':
	homework()










