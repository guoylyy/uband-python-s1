# !usr/bin/python
# -*- coding: utf-8 -*-
# @author: Xiaomu

# For beginner
# 1. variable - int,num,str,bool
# 2. if
# 3. > < >= <= ==
# 4. print

def main():
	who = '锅蜀黍老妈' 
	good_price  = 6
	good_description = '西双版纳大白菜'

	is_cheap = False
	reasonable_price = 5
	buy_amount = 2
	for good_price in range(1,6):
		for buy_amount in range(0,4):
			 good_price=good_price-1
			 buy_amount=buy_amount+1
	print '%s买了%d斤 '%(who,buy_amount)
if __name__ == '__main__':
  main()

