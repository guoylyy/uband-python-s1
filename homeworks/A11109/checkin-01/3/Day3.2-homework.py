#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: erhua


def accounting(is_cheap4, buy_amount4, total_price3)
	if is_cheap4:
		print '老妈记账今天买菜 %d 斤, 花了 %d 元' % (buy_amount4, total_price3)

		try:
			accounting(is_cheap4, buy_amount4, total_price2) #talk_with_daddy(is_cheap3, buy_amount3)
		except Exception,e:
			print '发生错误：%s' % (e)
	

def talk_with_daddy(is_cheap3, buy_amount3):
	if is_cheap3:
		print '老妈回到家里， 跟老爸说:"今天去买菜，价格不贵, 买了 %d 斤".' % (buy_amount3)
	else:
		print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买".'

def buybuybuy():
	good_price = 3
	reasonable_price = 5
	buy_amount = 2 + (reasonable_price - good_price)

	total_price = good_price * buy_amount

	who = 'erhua的老妈'
	good_description = "西双版纳大白菜"
	
	is_cheap = False

	print "%s上街看到了%s, 卖 %d 元/斤 " % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount = 2 + (reasonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了 %d 斤, 花了 %d 元' % (buy_amount, total_price)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买, 扬长而去'

	return is_cheap, buy_amount, total_price

def main():
	is_cheap2, buy_amount2 = buybuybuy()
	talk_with_daddy(is_cheap2, buy_amount2)
	accounting(is_cheap4, buy_amount4, total_price2)

if __name__ == '__main__':
  main()