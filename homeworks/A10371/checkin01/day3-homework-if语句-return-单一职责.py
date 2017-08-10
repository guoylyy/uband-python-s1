#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yuanzi

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 单一职责原则就是一个code block只做一件事
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 

def buy():
  good_price = 3 
  reasonable_price = 5
  buy_amount = 2

  who = '麻麻'
  good_description = '绿油油的大白菜'

  is_cheap = False
	
  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  if good_price <= reasonable_price:
  	print '她认为便宜'
  	is_cheap = True
  	buy_amount = 2 + (reasonable_price - good_price)
  	if buy_amount > 4:
  	  buy_amount = 4
  	print '她买了 %d 斤' % (buy_amount)
  else:
    print '她认为贵了'
    is_cheap = False
    print '她并没有买，扬长而去'	
  	
  return is_cheap, buy_amount, good_price

def talk_with_daddy(is_cheap3, buy_amount3):
  if is_cheap3:
    print '老妈回家跟老爸说：“今天买菜，价格便宜，买了 %d 斤。”' % (buy_amount3)
  else:
	print '老妈回家跟老爸说：“今天买菜，价格太贵，没买菜。”'

def record_account(buy_amount2, good_price):
  total_price = good_price * buy_amount2
  print '老妈在小本子上写买菜一共花了 %d 元' % (total_price)

def main():
    is_cheap2, buy_amount2, good_price = buy()

    talk_with_daddy(is_cheap2, buy_amount2)

    record_account(buy_amount2, good_price)


if __name__ == '__main__':
  main()


