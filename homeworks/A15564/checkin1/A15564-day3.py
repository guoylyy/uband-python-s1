#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: shangxindepidan

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
print '#1'

def buybuybuy():
	who = '伤心的皮蛋的老妈'
	good_price = 5
	good_description = "西双版纳大白菜"
	is_cheap = True 
	reasonable_price = 5 
	buy_amount = 2

	print "%s上街看到了%s, 卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜 '
		is_cheap = True
		buy_amount = 2 + (reasonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了 %d 斤 ' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去'
	
	return is_cheap, buy_amount

def talk_to_daddy(is_cheap3, buy_amount3):
	if is_cheap3:
		print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。' % (buy_amount3)
	else:
		print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。'

def main():
	is_cheap2, buy_amount2 = buybuybuy()
	talk_to_daddy(is_cheap2, buy_amount2)

if __name__ == '__main__':
	main()

print '###Question: why buy_amount(is_cheap)3 equals to buy_amount(is_cheap)2???'

# 2. 解释一遍自己眼中的单一职责原则是什么？
print '#2'
print 'A: One code block is literally responsible for one function, easy to quote for repetitive uses.'
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
print '#3'
def buybuybuy():
	who = '伤心的皮蛋的老妈'
	good_price = 3
	good_description = "西双版纳大白菜"
	is_cheap = True 
	reasonable_price = 5 
	buy_amount = 2

	print "%s上街看到了%s, 卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜 '
		is_cheap = True
		buy_amount = 2 + (reasonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了 %d 斤 ' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去'
	
	return is_cheap, buy_amount, good_price

def talk_to_daddy(is_cheap3, buy_amount3):
	if is_cheap3:
		print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。' % (buy_amount3)
	else:
		print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。'

def record_account(is_cheap4, buy_amount4, good_price4):
	if is_cheap4:
		print '老妈在小本子记了买菜花销 %d 元' % (buy_amount4 * good_price4)
	else:
		print '老妈很生气，没有记账'

def main():
	is_cheap2, buy_amount2, good_price2 = buybuybuy()
	talk_to_daddy(is_cheap2, buy_amount2)
	record_account(is_cheap2, buy_amount2, good_price2)

if __name__ == '__main__':
	main()

# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
# 
