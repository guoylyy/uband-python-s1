#!/usr/bin/python
# -*-coding: utf-8 -*-
# @author: Fangcheng
# 
def record_account(is_cheap2, buy_total2):
  if is_cheap2:
    print '老妈回到家里，在笔记本上记录:"今天去买菜，菜很便宜，花了 %d 元买菜"”。' %(buy_total2)
  else:
    print '老妈回到家里，在笔记本上记录:"今天去买菜，菜好贵额，没买"。'


def talk_with_daddy(is_cheap3, buy_amount3):
  if is_cheap3:
    print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。' %(buy_amount3)
  else:
    print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。'

def buybuy():
  who = 'fc的老妈 '
  good_price = 3  #小贩的价格
  good_description = "西双版纳大白菜" #小贩的招牌
 
  is_cheap = False #是否便宜
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤
 
  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)
 
  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    #解决老妈买几斤的问题
    #5-2 4-3 3-4 2-4
    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4:
      buy_amount = 4
    print '她买了 %d 斤' % (buy_amount)
    
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'
  buy_total =buy_amount * good_price
  print buy_total
 
  return is_cheap, buy_amount,buy_total
def main():
  is_cheap2, buy_amount2, buy_total2 = buybuy()
  talk_with_daddy(is_cheap2, buy_amount2)  
  
  record_account(is_cheap2, buy_total2)
 
if __name__ == '__main__':
  main()