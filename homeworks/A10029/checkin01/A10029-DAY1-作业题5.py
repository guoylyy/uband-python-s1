#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zi le

#开始我的表演
def main():
	who='梓乐的妈妈'
	good_description="大白菜"

	good_price=3.2
	reasonable_price=5
	buy_amount=2

	print "%s上街看到%s，卖%0.2f元/斤 "%(who,good_description,good_price)

	if good_price<=reasonable_price:
		print '她认为便宜'
		is_cheap=True
		if reasonable_price-1<good_price<=reasonable_price:
			print '她买了%d斤 '%(buy_amount)
		if reasonable_price-2<good_price<=reasonable_price-1:
			print '她买了%d斤 '%(buy_amount+1)
		if good_price<=reasonable_price-2:
			print '她买了%d斤 '%(buy_amount+2)
	else:
		print '她认为贵了'
		is_cheap=False
		print '她并没有买，转身离开了'	

if __name__ == '__main__':
  main()		

