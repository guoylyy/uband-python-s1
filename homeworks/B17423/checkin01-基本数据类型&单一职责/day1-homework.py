#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: seiya

#3. 让星矢的老妈买两斤白菜而不是扬长而去，修改good_price或reasonable_price使good_price <= reasonable_price

#4. 
# what's the meaning of 'number', 'string', 'boolean' in python?
# python的几种数据类型：数字，字符串，布尔值(True,False)
#try to describe the meaning of 'if' statement in your mind?
#条件判断语句。代码按条件执行
#Why we need > < == >= <= ...etc...?
#进行数据的比较，作为判断依据

#5. 小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
def main():
	who = '星矢的老妈'
	good_price = 4  #3.修改
	good_description = "西双版纳大白菜"

	is_cheap = False
	reasonable_price = 5
	buy_amount = 2
	max_amount = 4

	print ("%s上街看到了%s,卖%d元/斤" % (who, good_description, good_price))

	if good_price <= reasonable_price:
		print ('她认为便宜')
		is_cheap = True
		#5.修改
		print ('她买了%d 斤' % (min(max_amount, buy_amount + reasonable_price - good_price)))
	else:
		print ('她认为贵了')
		is_cheap = False
		print ('她并没有买，扬长而去')

#run function
if __name__ == '__main__':
	main()