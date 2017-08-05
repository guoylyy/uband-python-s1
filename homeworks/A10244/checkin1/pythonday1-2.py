# !usr/bin/python
# -*- coding: utf-8 -*-
# @author: Xiaomu

# For beginner
# 1. variable - int,num,str,bool
# 2. if
# 3. > < >= <= ==
# 4. print

def main():
	who = 'Master的老妈' 
	good_price  = 6
	good_description = '西双版纳大白菜'

	is_cheap = False
	reasonable_price = 5
	buy_amount = 2

	#prepare to run now !
	print "%s上街看到 %s,卖%d元/斤 " % (who,good_description,good_price)
	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		print '她买了%d斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她依然买了%d斤'%(buy_amount)
if __name__ == '__main__':
  main()

