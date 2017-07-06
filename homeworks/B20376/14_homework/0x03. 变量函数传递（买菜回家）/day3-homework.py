#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Emma


def jijiji(is_cheap,buy_amount,record_account,good_description):
   if is_cheap:
    print '老妈在小本子上记下账目：今天买了 %s ，花销 %d 元。' %(good_description,record_account)
   else:
    print 'nothing'

    
def talk_with_daddy(is_cheap,buy_amount):
   if is_cheap:
    print '老妈回到家里，跟老爸说：“今天去买菜，价格不贵，买了 %d 斤”。' %(buy_amount)
   else:
    print '老妈回到家里，跟老爸说：“今天去买菜，菜好贵额，没买”。'


def buybuybuy():
  who = '老妈'
  good_price = 3  
  good_description = "西双版纳大白菜" 
 
  reasonable_price = 5 
  buy_amount = 2

  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    buy_amount = 2 + (reasonable_price - good_price)
    record_account = (buy_amount * good_price)
    if buy_amount > 4:
      buy_amount = 4
    print '她买了 %d 斤' % (buy_amount)
  else:
    print '她认为贵了'
    is_cheap = False
    print '她并没有买，扬长而去'

  return is_cheap,buy_amount,record_account,good_description

def main():
  #买买买
  is_cheap,buy_amount,record_account,good_description = buybuybuy()
  #说说说
  talk_with_daddy(is_cheap,buy_amount)
  #记记记
  jijiji(is_cheap,buy_amount,record_account,good_description)

if __name__ == '__main__':
  main()