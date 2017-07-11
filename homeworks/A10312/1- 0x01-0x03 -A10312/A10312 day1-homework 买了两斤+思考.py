#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: wandou

# For beginner
# 1. variable - num,str,boolean
# 2. if
# 3. > < >= <= == 
# 4. print

def talk_with_daddy():
	if is_cheap:
		print '老妈回到家里，跟老爸说：“今天去买菜，价格不贵，买了两斤。”'
	else:
		print '老妈回到家里，跟老爸说：“今天去买菜，菜好贵啊，没买。”'

def buybuybuy():
	who = '豌豆的老妈 '
	good_price = 3 
	good_description = "西双版纳大白菜 "

	is_cheap = False
	reasonalbe_price = 5
	buy_amount = 2

 	print " %s上街看到了%s，卖 %d 元/斤 " % (who, good_description, good_price)

	if good_price <= reasonalbe_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount = 2 + (reasonalbe_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去'



# run function
if __name__ == '__main__':
  main()

# 思考： 
# 变量，是会影响并改变这组代码运行结果的因素
# if... if是条件？对变量的限定条件？
#  <= >= 这些符号是用于描述限定条件的...？