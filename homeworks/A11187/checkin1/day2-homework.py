#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xiangrikui

def main():
	book_number=8
	book_price=20.6
	pen_number=4
	pen_price=6.8

	#01. + - * / 
	book_and_pen_per_price_sum = book_price + pen_price
	print 'cost %d' % (book_and_pen_per_price_sum)
	book_and_pen_per_price_gap = book_price - pen_price
	print 'cost %g' % (book_and_pen_per_price_gap)
	book_total_price = book_price * book_number
	print 'cost %0.2f' % (book_total_price)
	pen_total_price = pen_price * pen_number
	print 'cost %0.2f' % (pen_total_price)
	book_per_price = book_total_price / book_number
	print 'cost %d' % (book_per_price)
	pen_per_price = pen_total_price / pen_number
	print 'cost %g' % (pen_per_price)

	#02. ** // % 
	number_1 = 3 ** 4
	print 'sum %d ' % (number_1)
	number_2 = 4 // 3.0
	print 'sum %d ' % (number_2)
	number_3 = -25.5 % 2.25
	print 'sum %g ' % (number_3)

	#03. & | 
	number_4 = 5 & 3
	print 'result %d ' % (number_4)
	number_5 = 5 | 3
	print 'result %d ' % (number_5)

	#04. > < >= <= 
	print 'test 1: %d' % (5 > 3)
	print 'test 2: %d' % (5 < 3)	
	print 'test 3: %d' % (4 >= 3)
	print 'test 4: %d' % (3 <= 6)
	
	#05. ==	!= 
	x = 3
	y = 2
	if x==y:
		print 'True '
	if x!=y:
		print 'False '

	#06.not and or 
	a = 6 > 8
	b = 7 <= 14
	if not a:
		print 'False a'
	
	if (a and b):
		print 'True a'
	else :	
		print 'True b'

	if (a or b):
		print 'ok'
	else:
		print 'over'

if __name__ == '__main__':
	main()