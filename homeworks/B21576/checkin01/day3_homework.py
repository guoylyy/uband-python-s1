#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: suancaiyu
# 学习内容：
#1,理解单一职责在编程中的应用 ：如果同一变量，代码，功能在程序中重复引用超过3次，可以将它们单独定义在一个函数(也就量函数封装)
#2，实现记账函数record_account 输出老妈买菜的花销 ,学习函数的调用，函数的传参，函数的返回值，对函数返回值的引用 
#3,实现函数定义老爸和老妈的对话，如果今天价格便宜就x斤，如果价格贵就不买 

def record_account(is_cheap2, good_price2, buy_amount3):
  if is_cheap2:
    record_account = good_price2 * buy_amount3

    print '妈妈回家拿出记账本，写下今天花了%d钱' % (record_account)


def talk_to_daddy(is_cheap3, buy_amount3):
  if is_cheap3:
    print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了%d斤”' % (buy_amount3)
  else:
    print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。'
	
def buybuybuy():
  good_price = 3   #是一个会变的数字，每降低1元，多买1斤
  reasonable_price = 5
  buy_amount = 2   #是一个会变的数字，每降低1元，多买1斤

  who = 'suancaiyu的妈妈'
  good_description = '西双版纳大白菜'

  is_cheap = False

  print '%s上街看到了 %s, 卖 %d 元/斤' % (who, good_description, good_price)

  if good_price <= reasonable_price:    # 这种结尾的冒号要特别注意，如果丢了的话要补上
    print '她认为很便宜'
    is_cheap = True

    #开始考虑买几斤的问题    5-2  4-3 3-4 2-4   最多买四斤
    buy_amount = 2 + (reasonable_price - good_price)

    if buy_amount > 4:
      buy_amount = 4

    print '她买了 %d 斤' % (buy_amount)
  else:
	print '她认为贵了'
	is_cheap = False
	print '她并没有买，扬长而去'

  return is_cheap, buy_amount, good_price

def main():
  is_cheap2, buy_amount2,good_price2 = buybuybuy()
  talk_to_daddy(is_cheap2, buy_amount2)
  record_account(is_cheap2, good_price2, buy_amount2)

if __name__ == '__main__':
  main()
