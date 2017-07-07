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
def is_even(num):
  if num % 2 == 0:
  	flag = True
  else:
  	flag = False
  return flag

def print_all_list(lst):
	
	for index, veg in enumerate(lst):
		print '第%d个菜是%s' %(index + 1, veg)
		#index += 1


def buy_no_odds(lst):  #独特的买菜模式，只买双数
	print '老妈来到菜市场'
	#index = 0
	for index,veg in enumerate(lst):
		if is_even(index):
			print '老妈看到%s,买了%d斤' % (lst[index], index + 1)
			#print '------------------'
			print '老妈继续逛...'

		else:
			print '老妈看到%s,不买' % lst[index]
		#index += 1


def buybuybuy():
	lst = ['白菜', '萝卜', '西红柿', '甲鱼', \
	'龙虾', '生姜', '白芍', '西柚', '牛肉', '水饺']
	print '原始菜单：'
	print_all_list(lst)
	print '-------------'



	# 01 买双数
	buy_no_odds(lst)


	# 02 加菜
	lst.append('莲藕')
	lst.append('苦瓜')
	lst.append('土豆')
	print '新菜单：'
	print_all_list(lst)
	print'——————————————————'

	# 03 只逛第 5~9 个菜
	buy_no_odds(lst[5:10])




if __name__ == '__main__':
	#print#      #为什么这里不打一行就运行不出结果呢？
	buybuybuy()