#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 

def buybuybuy():
	who = '0000的老妈'
	good_price = 5  #小贩的价格
	good_description = '西双版纳大白菜 ' #小贩的招牌

	is_cheap = False #是否便宜
	reasonable_price = 5 #老妈能接受的最高价格
	buy_amount = 2 #准备买两斤

	total_price = 0 #买菜一共花的钱

	print ' %s上街看到了%s,卖 %d 元/斤 ' %(who, good_description, good_price) 

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount = 2 + reasonable_price - good_price
		if buy_amount > 4:
			buy_amount = 4
		print '她买了 %d 斤' %(buy_amount)
		total_price = buy_amount * good_price
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去'

	return is_cheap, buy_amount, total_price, good_description, good_price,
def shuoshuoshuo(is_cheap3, buy_amount3):
	if is_cheap3:
		print '老妈回到家里，跟老爸说："今天去买菜，价格不贵，买了 %d 斤。"' %(buy_amount3)
	else:
		print '老妈回到家里，跟老爸说："今天去买菜，菜好贵啊，没有买。"'

def record_account(good_description3, good_price3,buy_amount3, total_price3):
	if total_price3 > 0:
		print '老妈拿出记账本，记录下"今天买%s, %d 元/斤，买了 %d 斤，一共花了 %d 元"'  %(good_description3,good_price3, buy_amount3, total_price3) 

def main():
	is_cheap2, buy_amount2, total_price2, good_description2, good_price2 = buybuybuy()
	shuoshuoshuo(is_cheap2,buy_amount2)
	record_account(good_description2, good_price2, buy_amount2, total_price2)

main()
