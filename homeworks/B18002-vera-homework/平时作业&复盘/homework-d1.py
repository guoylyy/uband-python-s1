#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: vera

def main ():
	who = 'Mom'
	good_price = 3
	good_description = "some cabbage" 

	is_cheap = False 
	reasonable_price = 5
	buy_amount = 2

	print '%s went to the market and saw %s sold at %d yuan/jin' % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print "She found them cheap."
		is_cheap = True
		buy_amount = (reasonable_price - good_price) + 2
		if buy_amount > 4:
		   buy_amount = 4
		print 'She bought %d jin.' % (buy_amount)
	else:
		print 'She found them expensive.'
		is_cheap = False
		print 'She went away without buying anything.'

if __name__ == '__main__':
	main ()