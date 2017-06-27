#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Liluo

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
def oddeven(index):
	#判断奇数偶数
	if index % 2==0:
		return True
	else:
		return False
def buy(decision,good_description,index): 
	#决定购买的输出
	if decision:
		buy_amount=index+1
		print "老妈看到%s，买了%g斤"%(good_description,buy_amount)
	else:
		print "老妈看到%s，不买"%(good_description)

def shopping(lst,start_index):
	print "老妈来到菜市场"
	for index,lst_item in enumerate(lst,start_index):
		decision=oddeven(index)
		buy(decision,lst_item,index)
		if index<len(lst)-1:
			print "老妈继续逛"
		else:
			print "老妈回家了"


def homework():
  lst=['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']
  shopping(lst,0)
  print '-----------------'
  lst1=['山药','猪蹄','苦瓜']
  lst.extend(lst1)
  shopping(lst,0)
  print '-------------------'
  lst2=lst[5:10]
  shopping(lst2,5)

if __name__ == '__main__':
  homework()