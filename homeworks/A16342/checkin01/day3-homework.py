#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yan

#单一职责原则：每一个代码块只处理一件事
def buy():
	who = 'yan的老妈'
	good_price = 2
	good_description = '西双版纳大白菜'

	is_cheap = False
	reasonable_price = 5
	buy_amount = 2
	print '%s上街看到了%s，卖%d元/斤' % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		diff = reasonable_price - good_price
		if diff >= 2:
			buy_amount = buy_amount + 2
			print '她买了%d斤' % (buy_amount)
		else:
			buy_amount = buy_amount + diff
			print '她买了%d斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'

	return is_cheap, buy_amount, good_price

def talk(is_cheap3,buy_amount3):

	if is_cheap3:
		print '老妈回到家，对老爸说：“菜不贵，我买了 %d 斤。”' % (buy_amount3) 
	else:
		print '老妈回到家，对老爸说：“菜好贵啊，我没有买。”'

def record(is_cheap3, buy_amount3, good_price3):
	spend = buy_amount3 * good_price3
	if is_cheap3:
		print '老妈在小本子记了买菜花销%d元' % (spend)


def main():
	is_cheap2, buy_amount2, good_price2 = buy()
	talk(is_cheap2, buy_amount2)
	record(is_cheap2, buy_amount2, good_price2)

if __name__ == '__main__':
	main()