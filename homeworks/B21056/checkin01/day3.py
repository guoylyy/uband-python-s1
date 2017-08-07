#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 

def keep_account(buy_amount4,good_price4):
	if good_price4 < 6:
		print '饼央翻开小本，工整得写到：“今日花费 %d 元。”' %(good_price4*buy_amount4)
	else:
		print '饼央翻开小本，工整得写到：“今日花费0元，减肥。”'

def talk_with_daddy(is_cheap3,buy_amount3):
	if is_cheap3:
		print '老妈回家跟老爸说：“今天菜不贵，买了 %d 斤。”' %(buy_amount3)
	else:
		print '老妈回家跟老爸说：“今天菜贵，没买，当减肥”'

def buybuybuy():

	good_price = 2   #每降低一元多买一斤
	reasonable_price = 5
	buy_amount = 2   #每降低一元多买一斤

	who = ' 饼央 '
	good_description = "西双版纳大白菜"

	is_cheap = False

	print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)
	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		#解决饼央买几斤
		#5-2 4-3 3-4 2-4 1-4
		buy_amount = 2 + (reasonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了 %d 斤' % (buy_amount) 
 	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去'

	return is_cheap,buy_amount,good_price
def main():
	#买买买
	is_cheap2, buy_amount2,good_price2 = buybuybuy()
	#说说说
	talk_with_daddy(is_cheap2,buy_amount2)
	#记记记
	keep_account(buy_amount2,good_price2)

if __name__ == '__main__':
 main()