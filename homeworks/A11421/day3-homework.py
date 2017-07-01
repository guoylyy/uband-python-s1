#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 
# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
# 

def tell_daddy(is_cheap, buy_amount, vege_name):
	if is_cheap:
		print '>>>> 麻麻回家告诉粑粑"今天%s老合算的，我买了%d斤"' % (vege_name, buy_amount)
	else:
		print ">>>> 麻麻回家告诉粑粑'今天%s太贵了，我木有买' " % (vege_name)

def buy():
	character = "麻麻"
	vege_name = "宇宙射线变种萝卜"

	unit_price = 4
	cheap_price = 2

	is_cheap = False

	print ">>>> %s在街上看到了%s，卖%d／斤" % (character, vege_name, unit_price)

	if unit_price <= cheap_price:
		is_cheap = True
		buy_amount = 2 + (cheap_price - unit_price)
		if buy_amount > 4:
			buy_amount =4
		total_spending = buy_amount * unit_price
		print ">>>> %s觉得便宜，她买了%d斤" % (character, buy_amount)
	else:
		is_cheap = False
		print ">>>> %s觉得小贩简直在抢钱，砍价无果，愤然离去" % (character)

	return is_cheap, buy_amount, total_spending, vege_name

def account(is_cheap, vege_name, total_spending):
	if is_cheap:
		print '>>>> 麻麻拿出账本，记录这笔花销："购买%s，总计花费%d元"' % (vege_name, total_spending)


def main():
	is_cheap, buy_amount, total_spending, vege_name = buy()
	tell_daddy (is_cheap, buy_amount, vege_name)
	account (is_cheap, vege_name, total_spending)

if __name__ == '__main__':
  main()