#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

def main():
	apple_number = 5
	apple_price = 4.8
	pie_number = 6
	pie_price = 6.7

	apple_total_price = apple_number * apple_price
	pie_total_price = pie_number * pie_price

	print 'pie cost %d ' % (pie_total_price)
	print 'pie cost %g ' % (pie_total_price)
	print 'pie cost %0.2f ' % (pie_total_price)

	number = 2**3
	print 'number = %d' % (number)

	print 'test: %d' % (1 != 2)
	print 'test: %d' % (1 >= 2)
	if 1:
		print 'goog'
	if 0:
		print 'xxx'

	if(2 != 2):
		print 'wweewe we w'


  

if __name__ == '__main__':
  main()