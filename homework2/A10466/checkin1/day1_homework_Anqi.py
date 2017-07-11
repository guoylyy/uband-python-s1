#!/usr/bin/python
#-*- coding: utf-8 -*-
# @author: anqi

def main():
	who = '安琪的老妈'
	good_price = 5
	good_description = "西双版纳大白菜"

	is_cheap= False
	reasonable_price = 6
	#t = reasonable_price-good_price
	buy_amount = 2
    
	print "%s上街看到了%s，卖%d元/斤" %(who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount=2+(reasonable_price-good_price)
		if buy_amount>4:
			buy_amount=4
		print "她买了%d斤"%(buy_amount)
	else:
		print '她认为贵了	'
		is_cheap = False
		print '她并没有买，扬长而去'

if __name__ == '__main__':
 	main()

#1 number是数字，string是字符串，boolean是逻辑判断
#2 if 判断是否符合条件，如果符合，运行下一步
#3 帮助具象化判断是否符合条件