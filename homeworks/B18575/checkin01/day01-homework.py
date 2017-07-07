#!/usr/bin/python
# -*- coding:utf-8 -*-
# @author:SKY


def main():
	who='SKY 的妈妈'
	good_price=4  #小贩的价格
	good_description='西双版纳大白菜' #小贩的招牌

	is_cheap=False  #是否便宜
	reasonable_price=5 # 老妈接受的价格
	buy_amount=2

	print "%s上街看到了 %s,卖 %d 元/斤 " % (who,good_description,good_price)
	buy_amount=buy_amount+cheap(good_price,reasonable_price)
	if good_price==reasonable_price:
		print "她认为便宜"
		is_cheap=True
		print "她买了 %d 斤" % (buy_amount)
	elif (good_price+1<=reasonable_price):
		print "她认为太便宜了"
		is_cheap=True
		print "她买了 %d 斤" % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap=False
		print "她并没与买，扬长而去"

#计算价格与妈妈的期望相差值，获得是否会多买，返回值是多买的数量，最大为2 
def cheap(good_price,reasonable_price):
	#因为最多买4斤，所以最多会多买2斤
	max_amount=2
	#商品价格比期望价格低
	if reasonable_price-good_price>0:
		if reasonable_price-good_price>max_amount:
			return max_amount
		else:
			return reasonable_price-good_price
	else:
		return 0



if __name__=='__main__':
	main()