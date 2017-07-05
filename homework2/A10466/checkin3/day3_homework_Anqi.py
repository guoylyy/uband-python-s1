#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Anqi
def talk_with_daddy(is_cheap3, buy_amount3):
  if is_cheap3:
    print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。' %(buy_amount3)
  else:
    print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵，没买"。'

def record_account(is_cheap3, good_price2, buy_amount3):
	if is_cheap3:
		print '老妈在小本子上记了买菜花销%s元'%(good_price2*buy_amount3)
	else:
		print '老妈没有花钱买菜'

def buybuybuy():
	good_price=3
	buy_amount=2
	reasonable_price=5

	who="安琪的老妈"
	good_description="西双版纳大白菜"

	is_cheap=False
	print "%s上街看到了%s，卖%d元/斤"%(who, good_description, good_price)

	if good_price<=reasonable_price:
		print "她认为便宜"
		is_cheap=True
		buy_amount=2+(reasonable_price-good_price)
		if buy_amount>4:
			buy_amount=4
		print "她买了%d斤"%(buy_amount)
	else:
		print '她认为贵了 '
    	is_cheap = False
    	print '她并没有买，扬长而去'

	return is_cheap, buy_amount, good_price

def main():
  is_cheap2, buy_amount2, good_price2 = buybuybuy()
  talk_with_daddy(is_cheap2, buy_amount2) 
  record_account(is_cheap2, buy_amount2, good_price2) 
if __name__ == '__main__':
  main()


