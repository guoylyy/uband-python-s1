#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yuanyi

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
#    我对单一职责的理解就是像机器零件一样，每一个部分只负责自己的任务，互不干扰，但互有合作
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 
# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
# 

def record_account(is_cheap4,buy_amount4):
	good_price	=	4
	if is_cheap4:
		money	=	buy_amount4	*	good_price
		print	'老妈在小本子记了买菜花销 	%d元'	%	(money)	
	else:
		print	'老妈今天买菜没花钱'

def talk_with_daddy(is_cheap3,buy_amount3):
	if is_cheap3:
		print	'老妈回到家里，跟老爸说："今天买菜，价格不贵，买了%d斤"。	'	%	( buy_amount3)
	else:
		print	'老妈回到家里，跟老爸说："今天买菜，菜好贵额，没买"。	'

def buybuybuy():
	good_price	=	4	#每降低一元，多买一斤
	reasonable_price	=	5
	buy_amount	=	2	#每降低一斤，多买一斤

	who	=	'源一的老妈'
	good_description	=	"西双版纳大白菜"

	is_cheap	=	False

	print	"%s上街看到了%s,	卖%d元/斤"	%(who,	good_description,	good_price)

	if good_price	<=	reasonable_price:
		print	'她认为便宜'
		is_cheap	=	True
		#解决老妈买几斤的问题
		#5-2 4-3 3-4 2-4
		buy_amount	=	2	+	(reasonable_price	-	good_price)
		if buy_amount	>	4:
			buy_amount	=	4
		print	'她买了%d斤'	%	(buy_amount)
	else:
		print	'她认为贵了	'
		is_cheap	=	False
		print	'她并没有买，扬长而去	'

	return	is_cheap,buy_amount
			

def main():
	is_cheap2,buy_amount2	=	buybuybuy()
 	talk_with_daddy(is_cheap2,buy_amount2)
 	record_account(is_cheap2,buy_amount2,)

if __name__ == '__main__':
	main()
