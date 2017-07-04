#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
#	我的理解是类似于分工一样，每个函数都有自己的职责，而且只需要有一种功能，完成一件事情，而不是既要
	#买菜，又要记录；我觉得这样应该是便于维护吧，那个地方出问题就找哪个地方，也可以避免找不到“责任人”
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 
# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
# 

def record_account(good_price, buy_amount):
	cost = good_price * buy_amount
	print '清蒸的妈妈在小本子上记了买菜花销 %d 元' % (cost)



def talk_to_dad(is_cheap,buy_amount):
	if is_cheap:
		print '清蒸的妈妈回到家里，跟老爸说：“今天去买菜，价格不贵，买了%d斤。开饭！”' % (buy_amount)
	else:
		print '清蒸的妈妈回到家里，跟老爸说：“今天去买菜，价格太贵，没买。不开饭了！”'
def buybuybuy():
	
	who = '清蒸的妈妈'
	good_description = "瓜州大白菜"

	good_price = 6 #商品价格
	resonable_price = 5
	buy_amount = 2

	is_cheap = False 

	#开始表演
	print "%s上街看到了%s ,卖 %d 元/斤" % (who, good_description, good_price)

	if  good_price <= resonable_price:
		print '她认为便宜'
		is_cheap = True
		#加分题
		buy_amount = buy_amount + (resonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		buy_amount = 0
		print '她并没有买，扬长而去 '

	return is_cheap,buy_amount,good_price

def main():
  is_cheap , buy_amount , good_price= buybuybuy()
  talk_to_dad(is_cheap , buy_amount)	
  record_account(good_price , buy_amount)

if __name__ == '__main__':
	main()