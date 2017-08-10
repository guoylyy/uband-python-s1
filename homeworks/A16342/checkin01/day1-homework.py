#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yan

def main():
	who = 'yan的老妈'
	good_price = 7
	good_description = '西双版纳大白菜'

	is_cheap = False
	reasonable_price = 5
	buy_amount = 2

	print '%s上街看到了%s，卖%d元/斤' % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		diff = reasonable_price - good_price
		if diff >= 2:
			buy_amount = buy_amount + 2
			print '她买了%d斤' % (buy_amount)
		else:
			buy_amount = buy_amount + diff
			print '她买了%d斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'

if __name__ == '__main__':
	main()