#!/usr/bin/python
# -*- coding: utf-8 -*-
# @autor:XXX

def buy():
	who = 'Mum'
	good_price = 1
	good_description = "西双版纳大白菜"

	is_cheap = False
	reasonable_price = $
	buy_amount = 2

	print "%s上街看到了%s，卖 %d 元／斤." %(who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜.'
		is_cheap = True
		if buy_amount+(reasonable_price - good_price)*1<=4:
			buy_amount=buy_amount+(reasonable_price- good_price)*1
		else:
			buy_amount=4

		print '她买了 %d 斤.' %(buy_amount)
	else:
		print ' 她认为贵了.'
		is_cheap= False
		print ' 她并没有买，扬长而去.'
	return buy_amount,is_cheap,good_price

def talk(buy_amount2,is_cheap2):
	if is_cheap2==True:
		print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。' %(buy_amount2)
	else:
		print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买."'

def record_account(buy_amount2,good_price2):
	print "老妈在小本子记了买菜花销 %d 元." % (buy_amount2*good_price2)

def main():
	buy_amount1,is_cheap1,good_price1=buy()
	talk(buy_amount1,good_price1)
	record_account(buy_amount1,good_price1)
#run function
if __name__=='__main__':
	main()
