#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yan

def main():
	#int float
	apple_number = 5
	apple_price = 4.8
	pie_number = 6
	pie_price = 6.7
	# + -
	total_number = apple_number + pie_number
	difference_number = pie_number - apple_number
	# * /
	apple_total_price = apple_number * apple_price
	pie_total_price = pie_number * pie_price
	print apple_total_price
	print pie_total_price
	average_price = (apple_total_price + pie_total_price)/total_number
	print average_price
	# ** power
	number = 2 ** 3
	print number
	# // %
	integer = 7 // 2
	residual = 7 % 2
	print integer
	print residual

	# 03
	print 'pie cost %d' % (pie_total_price)     #int
	print 'pie cost %g' % (pie_total_price)     #float
	print 'pie cost %0.2f' % (pie_total_price)  #小数点后两位

	# else
	print 'test: %d' % (1 != 2)
	print 'test: %d' % (1 >= 2)
	if 1:
		print 'lynn'

	if (2 != 2) or ( 1 <= 2):
		print 'yan'



if __name__ == '__main__':
	main()
