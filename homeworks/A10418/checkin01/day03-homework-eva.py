#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: eva

def shopping():
	good_price=5
	reasonable_price=5
	buy_amount=2
	total_expense=good_price*buy_amount

	is_cheap=False

	who='mom'
	good_description='high-quality cabbage'

	print'%s went to the street and saw %s selling for %d per kilogram'%(who,good_description,good_price)

	if good_price<=reasonable_price:
		print'she thought it was cheap'
		is_cheap=True
		buy_amount=2+(reasonable_price-good_price)
		if buy_amount>4:
			buy_amount=4
		print'she bought %d kilogram'%(buy_amount)
	else:
		print'she thought it was expensive'
		is_cheap=False
		print'she did not buy anything and left'

	return is_cheap,buy_amount,good_price,total_expense

def talk_with_dad(is_cheap,buy_amount):
	if is_cheap:
		print'mom went home and told dad that today she went to buy food, cabbage was not expensive,\
		so she bought %d kilogram'%(buy_amount)
	else:
		print'mom went home and told dad that today she went to buy food, cabbage was expensive,\
		so she did not buy' 

def record_account(is_cheap,buy_amount,good_price,total_expense):
	if is_cheap:
		print'mom wrote on the accounting booklet that she had bought %d kilograms cabbages\
		at the price of %d, the total expense is %d'%(buy_amount,good_price,total_expense)
	else:
		print'mom wrote nothing on the accounting booklet'

def main():
	is_cheap,buy_amount,good_price,total_expense=shopping()
	talk_with_dad(is_cheap,buy_amount)
	record_account(is_cheap,buy_amount,good_price,total_expense)




if __name__ == '__main__':
  main()



