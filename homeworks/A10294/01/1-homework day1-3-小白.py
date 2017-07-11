#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 小白

def record(is_cheap2, buy_amount2, good_price2):
  amount_price = buy_amount2*good_price2
  if is_cheap2:
    print '老妈在小本子写买菜共%d 元' %(amount_price)

def talk(is_cheap2, buy_amount2):
  if is_cheap2:
    print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了%d 斤”' %(buy_amount2)
  else:
    print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。' 

def buy():
  good_price = 5 #每降低一元，多买一斤
  reasonable_price = 5
  buy_amount2 = 2 #每降低一元，多买一斤
  
  who = '小白'
  good_description = "apple"

  is_cheap2 = False

  print "%s上街看到了%s，卖  %d 元/斤" %(who, good_description, good_price)
  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4:
      buy_amount = 4
    print '她买了 %d 斤' %(buy_amount)
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'
  
  return is_cheap, buy_amount, good_price

def main():
  is_cheap2, buy_amount2, good_price2 = buy()
  talk(is_cheap2, buy_amount2)
  record(is_cheap2, buy_amount2, good_price2)

if __name__ == '__main__':
  main()
#单一职责原则:定义的主体只有一个意义，与别的主体无关