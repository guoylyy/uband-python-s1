#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Stephy

def record_account(is_cheap4, buy_amount4, good_price3):
	if is_cheap4:
		print '今天花了 %d 元，老妈记在了账本上。' % (buy_amount4 * good_price3)

def talk_with_daddy (is_cheap3, buy_amount3):
	if is_cheap3:
		print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤' % (buy_amount3)
	else:
		print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。'	

def buybuybuy():
	good_price = 3
	resonable_price = 5
	buy_amount = 2
	who = '老妈'
	good_description = '西双版纳大白菜'
	is_cheap = True

	print '%s上街看到了%s，卖%d元/斤' % (who,good_description,good_price)
	if good_price <= resonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount = 2 + (resonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'	
	return is_cheap, buy_amount, good_price		
	
if __name__ == '__main__':
	is_cheap2, buy_amount2, good_price2 = buybuybuy()
	talk_with_daddy(is_cheap2, buy_amount2)
	record_account(is_cheap2, buy_amount2, good_price2)

