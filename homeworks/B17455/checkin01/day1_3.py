#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455
# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
def main():
  who = '我的妈妈'
  good_price = 4  #小贩的价格
  good_description = "西双版纳大白菜" #小贩的招牌
  price_gap = 0 #老妈认为合理价和小贩价的差价

  is_cheap = False #是否便宜
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤

  print "%s上街看到了%s，卖%d元/斤" % (who, good_description, good_price)

  price_gap = reasonable_price - good_price #计算差价

  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    if price_gap > 0:
    	buy_amount = buy_amount + price_gap
    if buy_amount >= 4:
    	buy_amount = 4

    print '她买了 %d 斤' % (buy_amount)
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'

if __name__ == '__main__':
  main()