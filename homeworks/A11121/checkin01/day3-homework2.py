#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Jinxiao

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# function(code block); one file multiple function(code block)
# return(pass variable)
# return multiple variables
# 2. 解释一遍自己眼中的单一职责原则是什么？
# single responsibility principle 每个代码块的职责是单一的，只执行一个任务，因此如果需要执行多个任务，即出现多项职责，则可以定义多个代码块。代码块之间可以进行单一/多个变量的调用传递return()
#3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 

def record_account(buy_amount4):
	print '老妈在小本子记了买菜花销%d元'%(buy_amount4)

def talk_with_daddy(is_cheap3, buy_amount3):
	if is_cheap3:
		print '老妈回到家里，跟老爸说:"今天去买菜，价格不贵，买了%d斤"。' %(buy_amount3)
	else:
		print '老妈回到家里，跟老爸说:"今天去买菜，菜太贵，没有买"。'


def buybuybuy():
	good_price = 4 #小贩的价格 每便宜1元，多买1斤
	reasonable_price = 5 #老妈觉得合适的价格
	buy_amount = 2 #准备买2斤,每便宜1元，多买1斤，最多买4斤

	who = '小金人的老妈'
	good_description = '西双版纳大白菜' #小贩的招牌

	is_cheap = False #是否便宜
	
	print '%s上街看到了%s,卖%d元/斤'% (who, good_description, good_price)
	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		#解决老妈买几斤的问题
		buy_amount = buy_amount + reasonable_price - good_price
		if buy_amount > 4:
			buy_amount = 4
		print '她买了%d斤'% (buy_amount)
	else:
		print '她认为贵'
		is_cheap = False
		print '她并没有买,扬长而去'

	return is_cheap, buy_amount

def main():	
	#买买买
	is_cheap2, buy_amount2 = buybuybuy()
	#说说说
	talk_with_daddy(is_cheap2, buy_amount2)
	#记记记
	record_account(buy_amount2)

if __name__ == '__main__':
  main()