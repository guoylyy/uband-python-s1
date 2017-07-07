#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Casey

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？答:[一段def 代码块 实现一个功能]
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 
# # 3天作业打卡方式 
# 1) 新建一个文件夹，学号-花名-03
# 2) 把 day1-homework  day2-homework day3-homework copy进去
# 3) 打包为 学号-花名-03.zip ,登陆网页版 web.gambition.cn 上传打卡
# 
def record_account(is_cheap, buy_amount, good_prise):
	#good_prise = 4

	if is_cheap:
		print '老妈在小本子记了买菜花销 %d 元' %(good_prise * buy_amount)
	else:
		pass

def talk_with_daddy(is_cheap, buy_amount):
    if is_cheap:
    	print '老妈回到家里,跟老爸说:"今天去买菜,价格不贵,买了 %d 斤."' %(buy_amount)
    else:
    	print '老妈回到家里,跟老爸说:"今天去买菜,菜好贵,没买."'	


def buy():
	good_prise = 4
	reasonable_price = 5
	buy_amount = 2

	who = '老妈'
	good_description = '大白菜'

	is_cheap = False


	try:
		talk_with_daddy(is_cheap, buy_amount)
	except Exception,e:
		print '发生错误'

	print "%s上街看到了 %s, 卖 %d 元/斤" % (who, good_description, good_prise)

	if good_prise <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount = 2 + (reasonable_price - good_prise)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'

	return is_cheap, buy_amount, good_prise #return需放最后，之后的代码不执行

def main(): #看代码先看主函数
	is_cheap, buy_amount, good_prise = buy() #先跑buy模块
 	talk_with_daddy(is_cheap, buy_amount)
 	record_account(is_cheap, buy_amount, good_prise)

 
if __name__ == '__main__':
  main()

