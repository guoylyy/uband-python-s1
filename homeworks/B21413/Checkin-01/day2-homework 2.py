#!/usr/bin/python
# -*- coding:utf-8 -*-

#1. variable - int,num,str,bool
#2. if
#3. > < >= <= ==
#4. print
def main():
  who = "一九零的老妈"
  good_price = 1 #小贩的价格
  good_description = "西双版纳大白菜" #小贩的招牌

  is_cheap = False #是否便宜
  reasonable_price = 4 #老妈能接受的最高价格
  buy_amount = 5  - good_price #准备买 2 斤

  # go 我们来走一组
  print '%s上街看到了%s, 卖 %d 元/斤' % (who, good_description, good_price)

  if good_price <= reasonable_price:
      print '她认为便宜'
      is_cheap = True
      print '她买 %d 斤' % (buy_amount)
  else:
      print "她认为贵了"
      is_cheap = False
      print "她并没有买，扬长而去"
if __name__ == '__main__':
    main()
