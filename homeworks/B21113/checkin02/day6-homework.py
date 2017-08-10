#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: eros

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
	print '老妈来到了菜市场,没有新菜，走了'
	lst	=	['白菜','萝卜','西红柿','甲鱼','龙虾','生姜','白芍','西柚','牛肉','水饺']	
	lst.append('土豆')
	lst.append('豆腐')
	lst.append('鱼肉')
	print '菜市场来了新菜，老妈又来逛菜市场'
	buybuybuy(lst)
 	print '老妈今天没空，决定选几个菜看看'
	lst_item=lst[4:9]
	buybuybuy(lst)

def buybuybuy(list_item):
	for index,item in enumerate(list_item):
		if(index%2==0):
			print '老妈看到了 %s,买了 %d 斤' %(item,index+1)
		else:
			print '老妈看到了 %s,没买' % (item)
		if(index==len(list_item)-1):
			print '老妈逛完了,回家了'
		else:
			print '老妈继续逛'
 
if __name__ == '__main__':
  homework()