#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tingting


# For beginner
# 1. variable - num,str,boolean
# 2. if
# 3. > < >= ==
# 4. print
def main():
  who = '亭亭的老妈'
  good_price = 6 #peddler's price
  good_description = '西双版纳大白菜'

  is_cheap = False #whether cheap
  reasonable_price = 6 #acceptable price
  buy_amount = 2 #1 kilogram

  #start
  #go
  print '%s上街看到了%s, 卖 %d元/斤' %(who, good_description, good_price)

  if good_price <= reasonable_price:
     print '她认为便宜'
     is_cheap = True
     print '她买了%d斤'%(buy_amount)
  else:
     print '她认为贵了'
     is_cheap = False
     print '她并没有买，扬长而去'

  #homework
  #1. see day1-homework.py

# run functon
if __name__ == '__main__':
   main()