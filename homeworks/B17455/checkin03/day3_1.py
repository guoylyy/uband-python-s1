#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455

# 1. function(code block)
#    one file multiple function(code block)
# 2. return (pass variable)
# 3. return mutiple variables
# 
# #原则# 单一职责原则
# 

def buybuybuy():

  good_price = 4  #小贩的价格
  # good_price = input('小贩的价格')
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤
  price_gap = 0 #老妈认为合理价和小贩价的差价

  good_description = "西双版纳大白菜" #小贩的招牌
  who = '我的妈妈'


  is_cheap = False #是否便宜


  print "%s上街看到了%s，卖%d元/斤" % (who, good_description, good_price)

  price_gap = reasonable_price - good_price #计算差价

  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    if price_gap > 0:
    	buy_amount = buy_amount + price_gap
    if buy_amount >= 4:
    	buy_amount = 4
    print '她买了%d斤' % (buy_amount)

  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'
  return is_cheap, buy_amount, good_price

def talk_with_dad(is_cheap3, buy_amount3, good_price3):
  if is_cheap3:
    print '妈妈回到家告诉爸爸:"今天菜挺便宜的，我买了菜，每斤才%d块钱，我买了%d斤呢"'% (good_price3, buy_amount3)
  else:
    print '妈妈回到家告诉爸爸:"今天菜好贵，我没买"'   

def accounting(is_cheap4, buy_amount4, good_price4):
  if is_cheap4:
    total_cost = good_price4 * buy_amount4
    print '老妈晚上记了笔账：今天买菜总共花了%d元' % (total_cost)



def main():
  #买菜
  is_cheap2, buy_amount2, good_price2 = buybuybuy()
  #交流
  talk_with_dad(is_cheap2, buy_amount2, good_price2)
  #记账
  accounting(is_cheap2, buy_amount2, good_price2)


if __name__ == '__main__':
  main()

  