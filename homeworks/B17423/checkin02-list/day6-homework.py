#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: seiya

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

def buyEven(lst):
	for index,it in enumerate(lst):
		if (index %2)==0:
			print ("买%s，%d斤" % (it, index+1))
		else:
			print ('不买%s' % it)
	
def print_lst(lst):
	print ("共%d种菜" % len(lst))
	for it in lst:
		print (it)

def homework():
  food = ['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
  print ("-----homework 1,买菜-----")
  buyEven(food)
  print ("-----homework 2,加菜-----")
  food.append('土豆')
  food.append('茄子')
  food.append('金针菇')
  print_lst(food)
  print ("-----homework 3, 切片------")
  food2=food[5:10]
  print_lst(food2)
  print ("1+2=",(1+2))

if __name__ == '__main__':
  homework()