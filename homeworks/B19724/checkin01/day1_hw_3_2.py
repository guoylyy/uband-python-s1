#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY

def main():
	who = "IPLAY的老妈"
	good_price = 6 
	good_description = "西双版纳大白菜"

	is_cheap = False
	reseasonable_price = 7 #修改理想价格，大于实际价格
	buy_amount = 2

	print "%s上街看到了%s，卖%s元/斤"%(who, good_description, good_price)

	if good_price <= reseasonable_price:
		print "她认为便宜"
		is_cheap =True
		print "她买了%s 斤" %(buy_amount)
	else:
		print "她认为贵了"
		is_cheap = False
		print "她并没有买，扬长而去"
if __name__ == "__main__":
	main()