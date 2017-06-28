#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yanyan



def main():
  who= '我的老妈'
  good_price= 4  #小贩的价格
  good_description = "西双版纳大白菜" #小贩的招牌

  is_cheap= False #是否便宜
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤


  print "%s 上街看到了 %s , 卖%d元一斤" % (who,good_description,good_price)
  if good_price<= reasonable_price:
    print '她认为很便宜'
    is_cheap= True
    print '她买了%d斤'% (buy_amount)
  else:
    print '她认为贵了'
    is_cheap= False
    print '她并没有买，扬长而去'
if __name__ == '__main__':
  main()

  #1.check
  #2.check
  #3.把good_price<=5或者reasonable price改成6
  #4.（1）number：数字，string：字符串，boolean：代表true or false（2）如果，代表了其中一种情况（3）需要经过比较后判断是否是在if的情况下，否则else
  #5

