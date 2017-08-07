#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: B17455
# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
def main():
  who = '我的妈妈'
  good_price = 5  #小贩的价格
  good_description = "西双版纳大白菜" #小贩的招牌

  is_cheap = False #是否便宜
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤


  print "%s上街看到了%s，卖%d元/斤" % (who, good_description, good_price)

  if reasonable_price >= good_price:
    print '她认为便宜'
    is_cheap = True
    print '她买了 %d 斤' % (buy_amount)
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'

if __name__ == '__main__':
  main()
