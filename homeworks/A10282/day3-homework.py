#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 233

# 1. 解释一遍自己眼中的单一职责原则是什么？
     #单一职责原则是指每段代码只为一个目的服务
     
# 2. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）
def record_account(is_cheap4, buy_amount4):
  if is_cheap4:
  	good_price = 4
  	money = good_price * buy_amount4
	print '老妈回到家里，在账本上记下："今天去买菜，花了 %g 元"。' %(money)

def talk_with_daddy(is_cheap3, buy_amount3):
  if is_cheap3:
	print '老妈回到家里，跟老爸说:"今天去买菜，价格不贵，买了 %d 斤"。' %(buy_amount3)
  else:
	print '老妈回到家里，跟老爸说:"今天去买菜，价格好贵，没有买"。'

def buybuybuy():
  good_price = 4  #小贩的价格
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤

  who = '233的老妈'
  good_description = "西双版纳大白菜" #小贩的招牌

  is_cheap = False #是否便宜
  
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

  return is_cheap, buy_amount

if __name__ == '__main__':
  is_cheap2, buy_amount2 = buybuybuy()
  talk_with_daddy(is_cheap2, buy_amount2)
  record_account(is_cheap2, buy_amount2)
