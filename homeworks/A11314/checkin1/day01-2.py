#!/usr/bin/python
# -*- coding: utf-8 -*-
# @autor:XXX

def main():
	who = 'Mum'
	good_price = 4 #'小贩价格'
	good_description = "西双版纳大白菜"

	is_cheap = False
	reasonable_price = 5 #'老妈能接受的最高价格'
	buy_amount = 2 #'老妈买的斤数'

	print "%s上街看到了%s，卖 %d 元／斤" %(who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		print '她买了 %d 斤' %(buy_amount)
	else:
		print ' 她认为贵了 '
		is_cheap= False
		print ' 她并没有买，扬长而去'


#run function
if __name__=='__main__':
	main()
