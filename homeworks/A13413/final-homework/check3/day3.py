#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: joylin

def  talk_with_daddy(is_cheap, buy_amount):
	if is_cheap:
		print '老妈回到家里，跟老爸说："今天去买菜，价钱不贵，买了 %d 斤。 "' %(buy_amount)
	else:
		print '老妈回到家里，跟老爸说："今天去买菜，菜好贵，没买"。'

def  record_account(good_name, cost):
	print '老妈记账：买了%s，共花了%d元' % (good_name, cost)

def buybuybuy():
	 who = 'joylin的老妈'
	 good_description = "西双版纳大白菜"
	 good_price = 3
	 reasonable_price = 5
	 buy_amount = 2
	 is_cheap = False
 
	 print "%s上街看到了%s, 卖 %d 元/斤" % (who, good_description, good_price)
	 if good_price <= reasonable_price:
			print '她认为便宜'
			is_cheap = True
			buy_amount = 2 + (reasonable_price - good_price)
			if buy_amount > 4:
				buy_amount = 4
			
			print '她买了%d斤' % (buy_amount)
			cost = buy_amount * good_price
	 else:
			print '她认为贵了'
			is_cheap = False
			print '她并没有买，扬长而去'

	 return is_cheap, buy_amount, cost, good_description
	

def main():
	is_cheap2, buy_amount2, cost, good_description = buybuybuy()
	talk_with_daddy(is_cheap2, buy_amount2)
	record_account(good_description, cost)
if __name__ == '__main__':
	main()