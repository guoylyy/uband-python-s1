#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: caramel

def main():
	apple_number = 5
	apple_price = 4.8
	pie_price = 6
	pie_number = 6.7

	appel_total_price = apple_number * apple_price
	pie_total_price = pie_number * pie_price 

 	print 'total cost %d ' % (appel_total_price + pie_total_price)
 	print 'margin cost %d ' % (pie_total_price - appel_total_price)

if __name__ == '__main__':
  main()