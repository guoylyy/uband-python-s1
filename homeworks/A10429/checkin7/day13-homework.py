#!/usr/bin/python
# -*- coding: utf-8 -*-
# 01.重复蜀黍代码
def main():
	week_overnight = [False,False,True,False,False]

	for index,is_overnight in enumerate(week_overnight):
		print '今天星期%d' %(index+1)

		try:
			overnight_check(is_overnight)
		except Exception,e:
			#发生错误的情况
			print '发生错误:%s' %(e)
		#else:
			#没有发生错误的情况
			#print '附带脚本'

def overnight_check(is_overnight):
	if is_overnight:
		raise Exception('离婚')
	else:
		print '正常 '

if __name__ == '__main__':
	main()
# 02.自己示例
def main():
	who = '那个谁的老妈'
	good_price = 6 #小贩的价格
	good_description = "西双版纳大白菜" #小贩的招牌

	is_cheap = False #是否便宜
	reasonable_price = 6 #老妈能接受的最高价格
	buy_amount = 2 #准备买2斤

	print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		try:
			print '她买了%d斤'  (buy_amount)
		except Exception,e:
			print '错误是:%s' %(e)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'
	print '报错测试成功'
if __name__ == '__main__':
	main()