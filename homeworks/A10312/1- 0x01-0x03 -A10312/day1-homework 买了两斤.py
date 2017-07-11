#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: wandou

# For beginner
# 1. variable - num,str,boolean
# 2. if
# 3. > < >= <= == 
# 4. print

def main():
	who = '豌豆的老妈'
	good_price = 5 
	good_description = "西双版纳大白菜"

	is_cheap = False
	reasonalbe_price = 5
	buy_amount = 2

 	print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonalbe_price:
		print '她认为便宜'
		is_cheap = True
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去'


	print '豌豆的老妈上街看到了西双版纳大白菜，卖 5 元/斤'
# run function
if __name__ == '__main__':
  main()

