#!/usr/bin/python
# -*- coding: utf-8 -*-

def buy():
	good_price = 4
	reasonable_price = 5
	buy_amount = 2
	

	who = 'mom'
	good_description = 'cabbage'

	is_cheap = False
	
	print '%s saw the %s on the street,the price of the cabbage is %d' % (who,good_description,good_price)
	if good_price <= reasonable_price:
		print 'she thought it was cheap '
		is_cheap = True
		buy_amount = 2 +(reasonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print 'she bought %0.1fkg' % (buy_amount/2.0)
		good_cost = buy_amount * good_price
	else:
		is_cheap = False
		print 'she thought it was too expensive,so she left away'
	return is_cheap,buy_amount,good_cost
def say(is_cheap2,buy_amount2):
	if is_cheap2:
		print 'she said to dad:\' the cabbage was cheap ,I bought %dkg\'' % (buy_amount2/2)
	else:
		print 'she said to dad:\' the cabbage was expensive,so I didn\'t buy any of it\''
def record_account(is_cheap2,good_cost2):
	if good_cost2>0:
		print 'she recorded the cots %d yuan on the paper' % (good_cost2)
	else:
		pass
		
def main():
	is_cheap2,buy_amount2,good_cost2= buy()
	say(is_cheap2,buy_amount2)
	record_account(is_cheap2,good_cost2)
if __name__ == '__main__':
	main()
	


	