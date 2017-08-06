#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 

def talk(is_cheap, buy_amount):
	if is_cheap:
		print 'Mother told father that the cabbages were good and she bought %d jins.'%(buy_amount)
	else:
		print 'Mother told father that the cabbages were too expensive so she did not buy them.'

def record_account(is_cheap, money_spent):
	if is_cheap:
		print 'Mother recorded that %d yuan was spent on the account book.'%(money_spent)

def buybuybuy():
	good_price=4
	reasonable_price=5
	buy_amount=2

	who='Mother'
	good_description='Terrific cabbages'

	is_cheap=False

	print '%s saw a board in the market, saying "The price of %s is %d yuan/jin". '%(who, good_description, good_price)

	if good_price<=reasonable_price:
		print 'She thought it was cheap.'
		is_cheap=True
		buy_amount=2+(reasonable_price-good_price)
		if buy_amount>4:
			buy_amount=4
		money_spent=buy_amount*good_price
		print 'She bought %d jins.'%(buy_amount)
	else:
		print "She thought it was too expensive."
		is_cheap=False
		print 'She left.'
		money_spent=0

	return is_cheap, buy_amount, money_spent

def main():
  is_cheap, buy_amount, money_spent=buybuybuy()
  talk(is_cheap, buy_amount)
  record_account(is_cheap, money_spent)
if __name__ == '__main__':
  main()

# Single responsibility principle means one funcion only deals with one goal you want to achieve.