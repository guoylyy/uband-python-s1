#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxh

def record_account(is_cheap4, buy_amount4, good_price4):
	if is_cheap4:
		print '老妈在小本子记了买菜花销 %d 元。' %(good_price4 * buy_amount4)
	else:
		print '老妈今天没花钱。'

def talktalktalk(is_cheap3, buy_amount3):
	if is_cheap3:
		print '老妈回到家里，跟老爸说:"今天去买菜，价格不贵，买了%d斤"。' %(buy_amount3)
	else:
		print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵，没买"。'

def buybuybuy():
	good_price = 4  #小贩的价格
	reasonable_price = 5 #老妈能接受的最高价格
	buy_amount = 2 #准备买 2 斤
	
	who = 'xxh的老妈'
	good_description = '小黄姜'

	is_cheap = False #是否便宜

	print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount = 2 + (reasonable_price - good_price)
		if buy_amount > 4:			
			buy_amount = 4

		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她扬长而去'

	return is_cheap, buy_amount, good_price, 

def main():
	is_cheap2, buy_amount2, good_price2 = buybuybuy()
	talktalktalk(is_cheap2, buy_amount2)
	record_account(is_cheap2, buy_amount2, good_price2)

# run function
if __name__ == '__main__':
	main()

#	#单一职责原则# 每一个子功能定义一个独立的函数来实现，设置好与其他函数的接口用来传递变量。