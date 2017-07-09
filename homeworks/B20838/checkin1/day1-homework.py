#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: lightningLUO

#task1.2.3

def buy():
  who = 'ligntningLUO的妈妈'
  good_price = 5 #小贩的价格
  good_description = "西双版纳大白菜" #小贩的招牌

  is_cheap = False #是否便宜
  reasonable_price = 5 #lightningLUO的妈妈能接受的最高价格
  buy_amout = 2 #准备买2斤



  print "%s有天上街看到了%s, 卖 %s 元/斤" % (who, good_description, good_price)

  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    print '所以买了%s斤' % (buy_amout)
  else:
    print '她认为贵了'
    is_cheap = False
    print '她并没有买，扬长而去'


# run function
if __name__ == '__main__':
  buy()



#task4"if是表示判断的语句;<>=等符号是表示判断条件


#task5 大白菜的价格以5元为基准，买2斤。每降低1元多买1斤，最多买4斤
def amount():
  good_price = 3
  reasonable_price = 5
  buy_amout = 2

  good_description = "西双版纳大白菜"

  is_cheap = False

  print '今天%s卖%s元/斤' % (good_description, good_price) 

  if good_price <= reasonable_price:
    print '便宜'
    is_cheap = True
    buy_amout = 2 + (reasonable_price - good_price)
    if buy_amout > 4:
      buy_amout = 4
    print '所以买%s斤'% (buy_amout)

  else:
    print '不划算'
    is_cheap = False
    print '下次买'

 #run function
if __name__ == '__main__':
  amount()











