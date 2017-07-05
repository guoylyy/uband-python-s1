#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 派
#以前是直接跟着简明教程的34页打的，现在根据github下载的day2进行学习


def main():
	#01.int
	apple_number = 5
	apple_price = 4.8
	pie_number = 6
	pie_price = 6.7

	#02
	apple_total_price = apple_number * apple_price
	pie_total_price = pie_number * pie_price

	#03. try to explain what's float
	print 'apple cost %d ' % (apple_total_price)
	print 'pie cost %g ' % (pie_total_price)
	print 'pie cost %0.2f ' % (pie_total_price)

	#04. 
	number = 2**3
	print 'number = %d ' % (number)

	#05
  	print 'test: %d' % (1 != 2)
  	print 'test: %d' % (1 >= 2)
  	if 1:
   			print 'good'
  	if 0:
    		print 'xxx'

  	if(2 != 2):
    		print 'well'



if __name__ == '__main__':
  main()

