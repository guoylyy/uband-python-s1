#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: SKY

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 单一职责，在某一代码块仅仅完成单一的任务。通过参数调用来实现多个代码块的交互。
# 代码逻辑会更加清晰，debug和后期维护会更有条理性
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 
# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
# 

#记账函数，参数为购买商品数量和商品价格
#在talk_with_daddy()函数中当is_cheap为TRUE时调用
def record_accound(buy_amount,good_price):
	account=buy_amount*good_price;
	print '老妈在小本子记了买菜花销 %d 元' %(account)

#与爸爸交谈函数
#参数为购买标志位，商品数量，商品价格
#当is_cheap为TRUE时会调用record_accound()函数,记账
def talk_with_daddy(cheap,buy_amount,good_price):
	if cheap:
		print '老妈回到家里，跟老爸说:"今天去买菜，价格不贵，买了 %d 斤".' %(buy_amount)
		record_accound(buy_amount,good_price)
	else:
		print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。'

#购物函数
#进行判断商品价格和老妈心中期望价格，若低于期望价格则购买，否则不买
def buybuybuy():
	good_price=5
	reasonable_price=5
	buy_amount=2

	who = 'SKY 的老妈'
	good_description = '西双版纳大白菜'

	is_cheap=False

	print '%s 上街看到了 %s ,卖 %d 元/斤 ' % (who,good_description,good_price)

	if good_price<=reasonable_price:
		print '她认为便宜'
		is_cheap=True
		buy_amount=2+(reasonable_price - good_price)
		if buy_amount>4:
			buy_amount=4
		print '她买了 %d 斤' % (buy_amount)
	else:
		is_cheap=False
		print '她认为贵了'
		print '她并没与买，扬长而去'
	talk_with_daddy(is_cheap,buy_amount,good_price)



#主函数，调用购物函数
def main():
  	buybuybuy()

#程序入口
if __name__ == '__main__':
  	main()