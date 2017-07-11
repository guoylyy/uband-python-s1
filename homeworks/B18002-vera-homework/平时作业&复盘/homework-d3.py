#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: vera

def buy():
	who = 'Mom'
	good_description = 'some cabbage'
	reasonable_price = 5
	is_cheap = False
	good_price = 3
	buy_amount = 2
	cost = buy_amount * good_price 

	print '%s went to market and saw %s sold at %d yuan/jin.' % (who, good_description, good_price)
	if good_price <= reasonable_price:
		print 'She found them cheap.'
		is_cheap = True
		buy_amount = (reasonable_price - good_price) + 2
		if buy_amount > 4:
			buy_amount = 4
		cost = buy_amount * good_price 	
		print 'She bought %d jin.' % (buy_amount)
	else:
		print 'She found them expensive.'
		is_cheap = False
		print 'She went away without buying anything.'

	return is_cheap, buy_amount, cost

def talk(is_cheap, buy_amount):
	if is_cheap:
		print 'She went home telling dad: \
"The cabbage were cheap and I bought %d jin."' % (buy_amount)
	else:
		print 'She went home telling dad: \
"The cabbage were so expensive that I did not buy any."'

def reccord_acount(is_cheap, buy_amount, cost):
	
	if is_cheap:
		print 'Then she noted down that the cost of cabbage was %d yuan.' % (cost)

def main():
	is_cheap, buy_amount, cost = buy()
	talk(is_cheap, buy_amount)
	reccord_acount(is_cheap, buy_amount, cost)


if __name__ == '__main__':
	main ()