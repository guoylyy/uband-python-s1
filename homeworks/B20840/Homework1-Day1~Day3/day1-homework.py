#!/usr/bin/python
#_*_ coding: utf-8 _*_
#@author: B20840

#For beginner
#1. variable - num, str, boolean
	#答：数字，字符串，布尔三种变量类型
#2. if
	#答：if 是条件判断语句，通常用来执行对某一条件的判断以及需要执行的相关语句；if....else....是它的基本结构，在if后通常紧
	#跟判断条件，在两个关键字的冒号后面通常是需要执行的相关语句
#3. > < >= <= ==
	#答：大于、小于、大于等于、小于等于、等于
#4. print
	#答：输出

def main():
	who='代码豆的亲妈'
	good_price = 6 #小贩的价格
	good_description = "西双版纳大白菜" #小贩的招牌

	is_cheap = False #是否便宜
	reasonable_price = 5 #老妈能接受的最高价格
	buy_amount = 2 #准备买2斤

	#开始你的表演
	#go 我们来走一组

	print "%s 上街看到 %s, 卖 %d 元/斤" %(who, good_description, good_price)

	#if good_price<=reasonable_price:
	#	print '她认为便宜'
	#	is_cheap = True
	#	print '她买了 %d 斤' %(buy_amount)
	#else:
	#	print '她认为贵了'
	#	is_cheap = False
	#	print '她并没有买，扬长而去'

	#第五题答案
	if good_price ==5:
		print '她认为便宜'
		is_cheap = True
		print '她买了 2 斤'
	elif good_price == 4:
		print '她认为便宜'
		is_cheap = True
		print '她买了 3 斤'
	elif good_price <= 3:
		print '她认为便宜'
		is_cheap = True
		print '她买了 4 斤'

	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'


	#homework
	#1. 看day1-homework.py

#run function
if __name__=='__main__':
	main()