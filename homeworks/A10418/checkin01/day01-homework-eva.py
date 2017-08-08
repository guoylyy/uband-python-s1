#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Eva


def main():
	who='妈妈'
	good_price=6 #小贩的价格
	good_description='西双版纳大白菜' #小贩的招牌

	is_cheap=False #是否便宜
	resonable_price=5 #妈妈能接受的最高价格
	buy_amount1=2 #准备买2斤
	

	print '%s上街看到了%s，卖 %d 元/斤' % (who, good_description, good_price)

	if good_price<=resonable_price:
		print '她认为便宜'
		is_cheap=True
		print '她买了 %d 斤' % (buy_amount1)
	else:
		print '她认为贵了'
		is_cheap=False
		print '她没有买，扬长而去' 

if __name__ == '__main__':
	main()

# day 1 note:
#回答下面几个问题
#1. what's the meaning of 'number', 'string', 'boolean' in python? 
#- number in python means the datatype of variables is number;
#- string means the type is character string;
#- boolean means is logical value

#2. try to describe the meaning of 'if' statement in your mind?
#- if statement is a function that judges True or False according to conditons
#and acts according to the results

#3. Why we need > < ==  >= <= ...etc...?
#- I guess it is bacause we need compare different things to know how to react

