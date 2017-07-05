#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: seiya

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 
# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
# 

#2. 不同的函数（代码块）实现不同的职责和功能，提高代码可读性和解耦，方便修改。
def record_account(account):
	print('老妈在小本子记了买菜花销%d元' % account)

def talk_with_daddy(is_cheap3, buy_amount3):
	if is_cheap3:
		print ('老妈回到家里，跟老爸说:"今天去买菜,价格不贵，买了%d斤"。' % buy_amount3)
	else:
		print ('老妈回到家里，跟老爸说:"今天去买菜,价格贵了，没买')

def buybuybuy():
	who = '星矢的老妈'
	good_price = 4
	good_description = "西双版纳大白菜"

	is_cheap = False
	reasonable_price = 5
	buy_amount = 2
	max_amount = 4

	print ("%s上街看到了%s,卖%d元/斤" % (who, good_description, good_price))

	if good_price <= reasonable_price:
		print ('她认为便宜')
		is_cheap = True
		#每降低一元，多买一斤
		buy_amount = buy_amount + reasonable_price - good_price
		buy_amount = min(max_amount, buy_amount)
		total_price = buy_amount * good_price;
		print ('她买了%d 斤' % (buy_amount))
		record_account(total_price)  #3. 记账
	else:
		print ('她认为贵了')
		is_cheap = False
		print ('她并没有买，扬长而去')

	return is_cheap,buy_amount

def main():
#买
  is_cheap2,buy_amount2=buybuybuy()
 #说
  talk_with_daddy(is_cheap2,buy_amount2)

if __name__ == '__main__':
  main()