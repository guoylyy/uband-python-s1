#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Guoshushu

# 1. function(code block)
#    one file multiple function(code block)
# 2. return (pass variable)
# 3. return mutiple variables
# 
# #原则# 单一职责原则
# 

def buybuybuy():
  good_price = 3 #每降低一元，多买一斤
  reasonable_price = 5
  buy_amount = 2 #每降低一元，多买一斤
  cost=good_price*buy_amount
  who = 'xiao的老妈 '
  good_description = "西双版纳大白菜"

  is_cheap1 = False

  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)
  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap1 = True
    #解决老妈买几斤的问题
    #5-2 4-3 3-4 2-4
    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4:
      buy_amount = 4
    print '她买了 %d 斤' % (buy_amount)
  else:
    print '她认为贵了 '
    is_cheap1 = False
    print '她并没有买，扬长而去'

  return is_cheap1, buy_amount,cost,good_description,good_price #这里不要忘了哦~其它地方要用到几个变量，这集就要return几个变量，注意不要改变量名
def main():                                                     #这里所有需要传递的变量后面要加一个数字标识符
  #买买买
  is_cheap11, buy_amount1,cost1,good_description1,good_price1= buybuybuy()
  #说说说
  talk_with_daddy(is_cheap11,buy_amount1)
  #记记记
  record_account(cost1,is_cheap11,buy_amount1,good_description1,good_price1)

def talk_with_daddy(is_cheap12, buy_amount2):                   #数字标识符编号再+1
  if is_cheap12:
    print '老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。' %(buy_amount2)
  
  else:
    print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。'
 
def record_account(cost2,is_cheap12,buy_amount2,good_description2,good_price2):
  if is_cheap12:
    print "老妈在小本子记:今天的%s %d元/斤，买了%d斤，买菜花销%d元. " % (good_description2,good_price2,buy_amount2,cost2)
  else:
    print "老妈没有记账"

if __name__ == '__main__':
  main()
