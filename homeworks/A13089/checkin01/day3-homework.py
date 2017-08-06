#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: pluto

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
def talk_with_daddy(is_cheap3,buy_amount3):
	if is_cheap3:
		print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了%d斤"。' %(buy_amount3)
	else:
		print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。'

def record_account(lalal):
	print '老妈在小本子记了买菜花销%d元' %(lalal)

def buybuybuy():
	who = '老妈'
	good_description = '西双版纳大白菜' #小贩的招牌

	reasonable_price = 5 #老妈能接受的最高价格
	buy_amount = 2 #每降低一元，多买一斤
	good_price = 2 #每降低一元，多买一斤

	is_cheap = False #是否便宜

	print '%s上街看到了%s，卖%d元一斤' % (who, good_description, good_price)
	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		#5-2 4-3 3-4 2-4
		buy_amount = 7 - good_price
		if buy_amount > 4:
			buy_amount = 4
		print '她买了%d斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'

	return is_cheap,buy_amount

def main():
  is_cheap2,buy_amount2 = buybuybuy() #买菜
  talk_with_daddy(is_cheap2,buy_amount2)	#说
  record_account(buy_amount2) #记账
if __name__ == '__main__':
  main()