#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: vera

def main():
	pencil_price = 3.2
	pencil_amount = 5
	pencil_total_price = pencil_price * pencil_amount

	pen_price = 6.1
	pen_amount = 2
	pen_total_price = pen_price * pen_amount

	total_amount = pencil_amount + pen_amount
	price_difference = pen_price - pencil_price
	ratio = pencil_price / pen_price

	print 'The pencils cost %d yuan.' % (pencil_total_price)
	print 'The pens cost %g yuan.' % (pen_total_price)
	print 'The pens cost %0.2f yuan.' % (pen_total_price)
	print 'We bought %d pens and pencils.' % (total_amount)
	print "The ratio of pencil's price to pen's is %0.6f." % (ratio)
	print 'The price difference of pen and pencil is %g yuan.' % (price_difference)

	x = 2**10
	print 'x = %d' % (x)

	if (3<=3):
		print 'haha'

	if (7!=11):
		print 'hhh233'

	x = 5
	y = 3
	if not (x == y):
		print "yeah"

	x = True
	y = False
	print x and y 
	print x or y

	print 2<<2
	print 11>>1
	print 5 & 3
	print 5 | 3
	print 5 ^ 3
	print ~ 5
 

if __name__ == '__main__':
	main ()

