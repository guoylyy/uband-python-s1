#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Anna

def jijiji(is_cheap, buy_amount, good_price):
	
	all_price = good_price * buy_amount

	if is_cheap:
		print '老妈在小本子记了买菜花销%d元 ' % (all_price)


def talktalktalk(is_cheap, buy_amount, good_price):

	if is_cheap:
		print '老妈回到家里，跟老爸说:"今天菜很便宜, 我买了%d斤"。' % (buy_amount)
	else:
		print '老妈回到家里，跟老爸说:"今天菜好贵，没买"。'
def maimaimai():	
	who = 'xiao的老妈 '
	good_price = 1 #会变
	reasonable_price = 5
	buy_amount = 2  #会变

	good_description = "西双版纳大白菜"

	is_cheap = False 
	

	print "%s上街看到了%s, 卖%d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
	  print "她觉着便宜" 
	  is_cheap = True
	  #5-2 4-3 3-4 2-4 
	  buy_amount = 2 + (reasonable_price - good_price)
	  if buy_amount > 4:
	  	buy_amount = 4
	  print '她买了%d斤 '% (buy_amount)
	else:
	  print "她认为贵了"
	  is_cheap = False
	  print "她没有买, 扬长而去"

	return is_cheap, buy_amount, good_price

# run function
if __name__ == '__main__':
  is_cheap, buy_amount, good_price = maimaimai()
  talktalktalk(is_cheap, buy_amount, good_price)
  jijiji(is_cheap, buy_amount, good_price)