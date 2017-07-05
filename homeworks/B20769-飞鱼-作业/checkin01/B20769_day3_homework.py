#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B20769-feiyu


# 1. function(code block)
#    one file multiple function(code block)
# 2. return (pass variable)
# 3. return mutiple variables
# 
# #原则# 单一职责原则！！！！！！！！！！！
# 单一职责原则即变量只在自己所在的代码块内起作用，不在与之无关的代码块内起作用。
def record_account(money3):
	print '老妈今天花了%d元钱' % (money3)

def talk_with_daddy(is_cheap3, buy_amount3):
  if is_cheap3:
    print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。' % (buy_amount3)
  else:
    print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。'

def buy_or_not():
	who = '我的老妈'
	good_price = 3  #小贩的价格
	good_description = "西双版纳大白菜" #小贩的招牌

	is_cheap = False #是否便宜
	reasonable_price = 5 #老妈能接受的最高价格
	buy_amount = 0

	print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount0 = 2+reasonable_price-good_price
		if buy_amount0 > 4:
			buy_amount = 4
		else:
			buy_amount = 2+reasonable_price-good_price
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去'
	money =	buy_amount * good_price
	return is_cheap , buy_amount , money  #返回值,返回值可被其他函数调用

def main():
	is_cheap2 , buy_amount2 ,money2 = buy_or_not()
	talk_with_daddy(is_cheap2 , buy_amount2)
	record_account(money2)
# run function
if __name__ == '__main__':
	main()
	

	