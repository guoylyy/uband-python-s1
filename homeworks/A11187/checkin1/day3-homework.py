#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author:xiangrikui

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？-------- answer: 针对某一相对独立的代码块，规定了某一特定变量后，该变量只在这一局部代码块行使职能进行运算，而不牵涉其余代码块
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 
# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
def shopping():
	reasonable_price = 5
	good_price = 4
	buy_amount = 2
	
	who = 'xiangrikui的妈妈 '
	good_description = "西双版纳大白菜"
	
	is_cheap = False 
	
	print "%s上街看到了%s，卖 %d 元/斤 " % (who, good_description, good_price)
	
	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount = 2 + (reasonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'

	return is_cheap, buy_amount, good_price

def talk(is_cheap3, buy_amount3):
	if is_cheap3:
		print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。' % (buy_amount3)
	else:
		print '老妈回到家里, 跟老爸说:"今天去买菜,菜好贵额,没买"。'

def record_account(is_cheap3, buy_amount3, good_price3):
	cost = buy_amount3 * good_price3
	
	if is_cheap3:
		print '老妈在小本子记了买菜花销 %0.2f元' % (cost)

def main():
	is_cheap2, buy_amount2, good_price2 = shopping()
	talk(is_cheap2, buy_amount2)
	record_account(is_cheap2, buy_amount2, good_price2)


if __name__ == '__main__':
	main()