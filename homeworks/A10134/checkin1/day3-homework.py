#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Liluo

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
def talk_with_dad(is_cheap1,buy_amount1):
	if is_cheap1:
		print 'Mom came back home and talked to dad:"今天去买菜，价格不贵，买了%0.2f斤"'%(buy_amount1)
	else:
		print 'Mom came back home and complained:"今天去买菜，菜好贵额，没买"'

def buy():
	good_price=9
	reasonable_price=5
	buy_amount=2
	buy_spending=0

	who="Liluo's Mon"
	good_description="西双版纳大白菜"

	is_cheap=False

	print " %s上街看到了%s，卖 %0.2f 元/斤 " % (who, good_description, good_price)

	if good_price<=reasonable_price:
		print "she thought it was cheap"
		is_cheap=True
		buy_amount=2+(reasonable_price - good_price)
		if buy_amount>4:
			buy_amount=4
		buy_spending=buy_amount*good_price
		print 'she bought %0.2f jin'%(buy_amount)
	else:
		print 'she thought it was expensive'
		is_cheap=False
		print 'she did not buy and went away'
	return is_cheap,buy_amount,buy_spending

# 2. 解释一遍自己眼中的单一职责原则是什么？
#一个程序中有多个功能时，最好把不同功能写在不同代码块中，更为高效和清晰
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
def record_account(buy_spending1):
	if buy_spending1>0:
		print "老妈在小本子记了买菜花销%0.2f元"%(buy_spending1)
# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
# 
def main():
	is_cheap2,buy_amount2,buy_spending2=buy()
	talk_with_dad(is_cheap2,buy_amount2)
	record_account(buy_spending2)
if __name__ == '__main__':
  main()