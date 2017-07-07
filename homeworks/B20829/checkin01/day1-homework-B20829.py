#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 派

 

def main():
  
  good_price = 1  #每降低一元，多买一斤
  reasonable_price = 5
  buy_amount = 2  #每降低一元，多买一斤
  
  who = '派的老妈'  
  good_description = "西双版纳大白菜"

  is_cheap = False 
  
     
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

  

# run function
if __name__ == '__main__':
  main()