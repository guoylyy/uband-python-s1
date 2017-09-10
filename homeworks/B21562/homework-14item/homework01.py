#!/usr/bin/python
# -*- coding:utf-8 -*-

# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
def main():
	who = "小狼" 
	mprice = 1  #小贩的价格每低1元
	mbuy = 1 #小狼多买1斤
	maxbuy = 4 #最多买4斤
	good_price = 4 #小贩的价格
	buy_amount = 5-good_price #购买的数量
	running = True

	# 开始我的表演
	# go 我们来走一组
	print "小贩的价格每低%d元，%s多买%d斤，最多买%d斤"%(mprice,who,mbuy,maxbuy)

	if good_price <= 4:
		print '小贩的价格为%d元，买了%d斤'%(good_price,buy_amount)
		
	else:
		print '贵了'
		print '不买'
	while running:
		realprice=good_price-1
		good_price=realprice
		realbuy=buy_amount+1
		buy_amount=realbuy
		if realbuy>4:
			print "最多只买4斤"
			running=False
		else:
			print "小贩的价格为%d元，买了%d斤"%(realprice,realbuy)

	#homework
	#1. 看 day1-homework.py

#run function
if __name__ == '__main__':
	main()