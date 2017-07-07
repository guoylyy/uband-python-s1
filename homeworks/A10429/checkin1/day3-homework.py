#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
#repeat guoshushu's code
def talk_with_daddy(is_cheap3, buy_amount3):
	if is_cheap3:
		print '老妈回到家里，跟老爸说：“今天去买菜，价格不贵，买了 %d 斤”。 ' %(buy_amount3)
	else:
		print '老妈回到家里，跟老爸说："今天去买菜，菜好贵额，没买"。 '

def buybuybuy():
	good_price = 3
	reasonable_price = 5
	buy_amount = 2

	who = 'xiao的老妈'
	good_description = '西双版纳大白菜'

	is_cheap = False

	print ' %s 上街看到了%s ,卖 %d 元/斤 ' % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜 '
		is_cheap = True
		buy_amount = 2 + (reasonable_price -good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了%d斤 ' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去 '

	return is_cheap, buy_amount

def main():
	is_cheap2, buy_amount2 = buybuybuy()
	talk_with_daddy(is_cheap2, buy_amount2)

if __name__ == '__main__':
	main()
# 2. 解释一遍自己眼中的单一职责原则是什么？
#回答：单一职责原则，意思是一个函数或者代码块，只做一件事情，不要多个任务放在一个函数里，比如买菜,回家跟老爸聊
#记账都分不同函数来执行，这样清晰明了，逻辑清楚，程序可读性似乎更好。

# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
def record_account(is_cheap4, buy_amount4, good_price4):
	if is_cheap4:
		total_price = (good_price4)*(buy_amount4)
		print '老妈在小本上记了买菜花销%d元 ' % (total_price)

def talk_with_daddy(is_cheap3, buy_amount3):
	if is_cheap3:
		print '老妈回到家里，跟老爸说：“今天去买菜，价格不贵，买了 %d 斤”。 ' %(buy_amount3)
	else:
		print '老妈回到家里，跟老爸说："今天去买菜，菜好贵额，没买"。 '

def buybuybuy():
	good_price = 3
	reasonable_price = 5
	buy_amount = 2

	who = 'xiao的老妈'
	good_description = '西双版纳大白菜'

	is_cheap = False

	print ' %s 上街看到了%s ,卖 %d 元/斤 ' % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜 '
		is_cheap = True
		buy_amount = 2 + (reasonable_price -good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了%d斤 ' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去 '

	return is_cheap, buy_amount, good_price

def main():
	is_cheap2, buy_amount2, good_price2 = buybuybuy()
	talk_with_daddy(is_cheap2, buy_amount2)
	record_account(is_cheap2, buy_amount2, good_price2 )

if __name__ == '__main__':
	main()

#
# 
# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
# 
def main():
  print 'test'
  pass

if __name__ == '__main__':
  main()