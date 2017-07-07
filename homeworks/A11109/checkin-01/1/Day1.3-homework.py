#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: erhua

def main():
	who = 'erhua的老妈'
	good_price = 3
	good_description = "西双版纳大白菜"

	is_cheap = False
	reasonable_price = 5
	
	fixed_amount = 2
	max_amount = 4
	difference = reasonable_price - good_price
	buy_amount = fixed_amount + difference

	print "%s上街看到了%s, 卖 %d 元/斤 " % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		if buy_amount <= max_amount:
			is_cheap = True
			print '她买了 %d 斤' % (buy_amount)
		else:
			print '她买了 %d 斤' % (max_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买, 扬长而去'

if __name__ == '__main__':
  main()