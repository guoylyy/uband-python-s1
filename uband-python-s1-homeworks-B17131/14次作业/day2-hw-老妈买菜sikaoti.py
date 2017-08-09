#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: youngmpjlt


#加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
#（1）这个是在老妈买的前提下，所以所做更改只需在if good_price <= resonable price 下面即可。
#（2）既然老妈都买了，那么最高的价格肯定从5开始，因为5是老妈至多可以接受的价格。5块钱， 根据原题目，是买两斤。（因为它还没有降低价钱）。4元时才会多买一斤变成3斤因为减了一元。
#（3）以此类推。可以推出公式。
def main():
	good_price = 4  #每降低一元，多买一斤
	reasonable_price = 5 
	buy_amount = 2 #每降低一元，多买一斤


	who = '片寄的老妈'
	good_description = "西双版纳大白菜" 

	is_cheap = False 

	print "%s上街看到了%s, 卖%d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount = 2 + (reasonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了%d 斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'

if __name__ == '__main__':
  main()
 