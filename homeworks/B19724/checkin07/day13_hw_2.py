#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY

def buy():
	good_price = 3
	reseasonable_price = 5
	buy_amount = 2

	who = "IPLAY的老妈 "
	good_description = " 西双版纳大白菜 "

	is_cheap = False

	print "%s 上街看到了 %s， 卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reseasonable_price:
		print "她认为便宜"
		is_cheap = True
		buy_amount = 2 + (reseasonable_price - good_price) #重新定义了buy_amount
		if buy_amount > 4:
			buy_amount = 4 #buy_amount 赋值，省略else
		print "她买了 %d 斤" % (buy_amount)
	else:
		print "她认为贵了"
		is_cheap = False
		print "她并没有买，扬长而去"
	#return is_cheap, buy_amount, good_price #使得这两个值能够重复利用
	
def main():
	#is_cheap, buy_amount = buy() #这两个值来自buy语块中
	#talk_with_dad(is_cheap,buy_amount) #把数值调用到talk_with_dad中
	try:
		buy()
	except Exception as e:
		print '发生错误'
	else:
		print '正常'
	
	try:
		talk_with_dad(is_cheap,buy_amount)
	except Exception as e:
		print '发生错误'
	else:
		print '正常' 
	pass
	
def talk_with_dad(is_cheap,buy_amount): #由于return 函数值的作用（传递变量）
	if is_cheap:
		print "老妈回到家里，跟老爸说：“今天去买菜，价格不贵，买了 %d 斤。”" % (buy_amount)
	else:
		print "老妈回到家里，跟老爸说：“今天去买菜，菜好贵额，没买。”"

if __name__ == "__main__":
	main()