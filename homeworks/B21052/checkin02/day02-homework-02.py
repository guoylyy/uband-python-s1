#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: caramel

def main():
	total_money = 100
	apple_price = 5
	pie_price = 20

	total_number = total_money / (apple_price + pie_price)	

	print 'total_number %s ' % (total_money / (apple_price + pie_price))

if __name__ == '__main__':
  main()