#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

def buybuybuy():
	who = '0000的老妈'
	good_price = 5  #小贩的价格
	good_description = '西双版纳大白菜 ' #小贩的招牌

	is_cheap = False #是否便宜
	reasonable_price = 5 #老妈能接受的最高价格
	buy_amount = 2 #准备买两斤

	total_price = 0 #买菜一共花的钱

	print ' %s上街看到了%s,卖 %d 元/斤 ' %(who, good_description, good_price) 

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount = 2 + reasonable_price - good_price
		if buy_amount > 4:
			buy_amount = 4
		print '她买了 %d 斤' %(buy_amount)
		total_price = buy_amount * good_price
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去'

	return buy_amount, total_price, good_description, good_price,


def record_account(good_description3, good_price3,buy_amount3, total_price3):
	if total_price3 > 0:
		print '老妈拿出记账本，记录下"今天买%s, %d 元/斤，买了 %d 斤，一共花了 %d 元"'  %(good_description3,good_price3, buy_amount3, total_price3) 

def main():
	buy_amount2, total_price2, good_price2, good_description2 = buybuybuy()
	try:
		record_account(good_description2, good_price2, buy_amount2, total_price2)
	except Exception,e:
		print 'error: %s ' %(e)

main()
