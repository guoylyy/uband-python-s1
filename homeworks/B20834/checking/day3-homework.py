#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
#答： 我的理解是每一段代码只完成一个单一的功能，将一个问题划分成不同的模块，用模块化程序的解决一个问题。
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 
# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
# 
def buybuybuy():
	who = '晨曦的妈妈'
	sold_product = '西双版纳的大白菜 '
	sold_price = 5
	acceptable_price = 5
	buy_amount = 2
	max_amount = 4
	is_cheap = False
	print '%s走在街上看到%s, 卖%d元/斤 ' % (who,sold_product,sold_price)
	if sold_price > acceptable_price :
		is_cheap = False
		print '老妈认为太贵, 她并没有买, 扬长而去 '
	else :
		#5-2 4-3 3-4 2-4
		is_cheap = True
		buy_amount = buy_amount + (acceptable_price - sold_price)
		if buy_amount > max_amount :
			buy_amount = 4
		print ' 老妈认为不贵, 老妈买了%d斤 ' % (buy_amount)
	return is_cheap,buy_amount,sold_price
			
def talk(is_cheap,buy_amount):
	if is_cheap:
		print '老妈和老爸说今天菜很便宜, 她买了%d斤' % (buy_amount)
	else :
		print '老妈和老爸说今天菜很贵，她没有买 '
def record_account(buy_amount,sold_price):
	buy_expense = buy_amount*sold_price
	print '老妈在小本子记了买菜花销%d元 ' % (buy_expense)

def main():
  is_cheap,buy_amount,sold_price = buybuybuy()
  talk(is_cheap,buy_amount)
  record_account(buy_amount,sold_price)

if __name__ == '__main__':
  main()