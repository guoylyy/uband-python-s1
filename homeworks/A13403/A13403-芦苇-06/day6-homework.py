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
  for lst_item in lst:  #遍历
    print ' %s '% (lst_item)

def main():
 print '老妈来到菜市场'
 lst = ['白菜', '萝卜', '西红柿', '甲鱼', '龙虾','生姜', '白芍', '西柚', '牛肉', '水饺'] #作业一
 for index,lst_item in enumerate(lst):
 	if index % 2 == 0:
		print '老妈看到 %s , 买了 %d 斤, 继续逛' %(lst_item, index+1)
 	else:
		print '老妈看到 %s , 不买, 继续逛' %(lst_item)


 print '----------' #作业二

 lst.append('香菜')
 lst.append('生菜')
 lst.append('芹菜')
 print_list(lst)

 print '----------' #作业三

 lst2 = lst[4:9]
 index = 0
 for index,lst_item in enumerate(lst2):
 	if index % 2 == 0:
 		print '老妈看到 %s , 买了 %d 斤, 继续逛' %(lst_item, index)
 	else:
 		print '老妈看到 %s , 不买, 继续逛' %(lst_item)
 	

if __name__ == '__main__':
	main()