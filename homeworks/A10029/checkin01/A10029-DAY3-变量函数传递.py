#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zi le

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 
# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡



#题2.单一职责原则就是一个设定好的变量，只在当前代码块中运行，只对其所在的代码块负责，并不会影响到其他的代码块。
def buy():
	who='梓乐的妈妈 '
	good_description="大白菜 "

	good_price=4.5
	reasonable_price=5
	buy_amount=2

	print "%s上街看到%s，卖%0.2f元/斤 "%(who,good_description,good_price)

	if good_price<=reasonable_price:
		print '她认为便宜 '
		is_cheap=True

		buy_amount=int(2+(reasonable_price - good_price))
		if buy_amount>4:
			buy_amount=4
		print '她买了%d斤 '%(buy_amount)	
	else :
		print '她认为贵了 '
		is_cheap=False
		print '她并没有买，扬长而去 '

	return is_cheap,buy_amount,good_price
	
def talk(is_cheap1,buy_amount):
	if is_cheap1:
		print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。'%(buy_amount)
	else :
		print '老妈回到家里，跟老爸说:“今天去买菜，菜好贵额，没买”。'	

def record_account(good_price,buy_amount,is_cheap):
	cost=good_price*buy_amount

	if is_cheap:
		print '老妈在小本子记了买菜花销%0.2f元 '%(cost)

def main():
	is_cheap,buy_amount,good_price=buy()
	talk(is_cheap,buy_amount)
	record_account(good_price,buy_amount,is_cheap)	


if __name__ == '__main__':
  main()