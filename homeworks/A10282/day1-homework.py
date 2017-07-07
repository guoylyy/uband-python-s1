#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 233

# 1 把锅蜀黍的老板改成你老妈，跑通
def main():
  who = '2333的老妈 '
  good_price = 6  #小贩的价格
  good_description = "西双版纳大白菜" #小贩的招牌

  is_cheap = False #是否便宜
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤

  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  
  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    print '她买了 %d 斤' % (buy_amount)
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'


if __name__ == '__main__':
  main()


# 2 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
def main():
  who = '2333的老妈 '
  good_price = 5  #小贩的价格
  good_description = "西双版纳大白菜" #小贩的招牌

  is_cheap = False #是否便宜
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤

  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  
  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    print '她买了 %d 斤' % (buy_amount)
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'


if __name__ == '__main__':
  main()
  
# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
  #变量：变量的值可以变化，既可以储存信息，又可以对变量进行操作
  #if：用来检验一个条件，如果条件为真，就运行if-块，而且在结尾处有个冒号表示下面跟着一个语句块
  #<=：小于等于
  #>=：大于等于

# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
def main():
  who = '2333的老妈 '
  good_price = 3  #小贩的价格
  good_description = "西双版纳大白菜" #小贩的招牌

  is_cheap = False #是否便宜
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤

  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  
  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4:
      buy_amount = 4
    print '她买了 %d 斤' % (buy_amount)
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'


if __name__ == '__main__':
  main()