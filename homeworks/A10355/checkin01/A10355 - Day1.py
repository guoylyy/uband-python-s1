#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxh

def main():
	who = 'xxh的老妈'
	good_price = 10  #小贩的价格
	good_description = '小黄姜'

	is_cheap = False #是否便宜
	reasonable_price = 5 #老妈能接受的最高价格
	buy_amount = 2 #准备买 2 斤

	print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount = 2 + (reasonable_price - good_price)
		if buy_amount > 4:			
			buy_amount = 4
		#if good_price == reasonable_price:
		#	buy_amount = buy_amount
		#if good_price == reasonable_price-1:
		#	buy_amount = buy_amount+1
		#else:
		#	buy_amount = buy_amount+2

		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她扬长而去'


# run function
if __name__ == '__main__':
	main()