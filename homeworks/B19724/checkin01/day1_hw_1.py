#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY

# For beginner
# 1. variable - num,str,boolean
# 2. if
# 3. > < >= <= == 
# 4. print
def main():
	who = " 锅蜀黍的老妈 "
	good_price = 6 #小贩的价格
	good_description = " 西双版纳大白菜 " #小贩的招牌

	is_cheap = False #是否便宜
	reseasonable_price = 5 #老妈能接受的最高价格
	buy_amount = 2 #准备买 2 斤
	# 开始你的表演
	# go 我们来走一组
	print "%s上街看到了%s，卖%s元/斤"%(who, good_description, good_price)

	if good_price <= reseasonable_price:
		print "她认为便宜"
		is_cheap =True
		print "她买了%s 斤" %(buy_amount)
	else:
		print "她认为贵了"
		is_cheap = False
		print "她并没有买，扬长而去"

# run function
if __name__ == "__main__":
	main()
