#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Anna

# For beginner
# 1. variable - num,str,boolean
# 2. if
# 3. > < >= <= ==
# 4. print
def main():	
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

# run function
if __name__ == '__main__':
  main()