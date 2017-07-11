#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: lightningLUO




#大白菜的价格以5元为基准，买2斤。每降低1元多买1斤，最多买4斤
def amount():
  good_price = 3
  reasonable_price = 5
  buy_amout = 2

  good_description = "西双版纳大白菜"

  is_cheap = False

  print '今天%s卖%s元/斤' % (good_description, good_price) 

  if good_price <= reasonable_price:
    print '妈妈觉得便宜'
    is_cheap = True
    buy_amout = 2 + (reasonable_price - good_price)
    if buy_amout > 4:
      buy_amout = 4
    print '决定买%s斤'% (buy_amout)

  else:
    print '妈妈觉得不划算'
    is_cheap = False
    print '决定下次买'


  return is_cheap, good_price, buy_amout, 


def talk_with_daddy(is_cheap3, good_price3, buy_amount3):
  if is_cheap3:
    print '回到家里，跟爸爸说:“今天去买西双版纳大白菜，价格不贵%s元/斤，买了%d 斤”。' % (good_price3, buy_amount3)
  else:
    print '回到家里，跟爸爸说:"今天去买西双版纳大白菜，菜好贵，没买"。'

  return is_cheap3, good_price3, buy_amount3


def record(is_cheap5, good_price5, buy_amount5):

  cost = good_price5 * buy_amount5 
  if is_cheap5:
    print '并在小本子记了买菜花销 %s 元' % (cost)
  else:
    print '不记账'
  return cost
  

def main():
  #买多少
  is_cheap2, good_price2, buy_amount2 = amount()
  #叙述
  talk_with_daddy(is_cheap2, good_price2, buy_amount2)
  #记录
  record(is_cheap2, good_price2, buy_amount2)
 
#run function
if __name__ == '__main__':
  main()


#单一职责原则就是每个模块的功能清晰唯一，一个模块完成一个功能。逻辑清晰明了