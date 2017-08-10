#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tangxiaocu

def main():
	#01.int
	apple_number = 5
	apple_price =4.8
	pie_number = 6
	pie_price = 6.7

	#02. * /
	apple_total_price = apple_number * apple_price
	pie_total_price = pie_number * pie_price

	#03. try to explain what's float
	print 'pie cost %d ' % (pie_total_price)
	print 'pie cost %g ' % (pie_total_price)
	print 'pie cost %0.2f ' %(pie_total_price)

	#04. **
	number = 2**3
	print 'number = %d' % (number)

#come on
if __name__ == '__main__':
	main()
