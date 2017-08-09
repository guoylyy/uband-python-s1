#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
#答：每一个函数块负责一个单独的功能实现
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
# 
def record_account(good_price,buy_amount):
  total = good_price * buy_amount
  return total

def talk_with_daddy(is_cheap, buy_amount):
  if is_cheap:
    print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。' %(buy_amount)
  else:
    print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。'

def buybuybuy():
  good_price = 3 
  reasonable_price = 5
  buy_amount = 2 
  who = 'xiao的老妈'
  good_description = "西双版纳大白菜"

  is_cheap = False

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

  return is_cheap, buy_amount,good_price

def main():
  is_cheap, buy_amount,good_price = buybuybuy()
  talk_with_daddy(is_cheap, buy_amount)  
  total1 = record_account(good_price,buy_amount)
  print "老妈在小本子记了买菜花销%s元" % (total1)
if __name__ == '__main__':
  main()
