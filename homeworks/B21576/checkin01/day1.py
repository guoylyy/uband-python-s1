#!/usr/bin/python
#-*-coding:utf-8 -*-
#author:suancaiyu
#学习内容：了解python 变量(数值和字符串)，if,print,编程的实质

def main():
  who = 'suancaiyu的老妈'
  good_price = 6        #或者把商品价格改成5。 
  good_description = "西双版纳大白菜"

  is_cheap = False
  reasonable_price = 5  #把这个合理价格改成6
  buy_amount = 2


  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  if good_price <= reasonable_price:
	  print '她认为很便宜'
	  is_cheap = True
	  print '她买了%d斤' % (buy_amount)
  else:
	  print '她认为贵了'
	  is_cheap = False
	  print '她并没有买，扬长而去'


if __name__ == '__main__':
  main()
	
