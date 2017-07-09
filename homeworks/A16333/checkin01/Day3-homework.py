#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: chendasuan

#1.function(code block)
#2.ruturn (pass varialbe)
#3.ruturn multiple variables
#原则# 单一职责原则

def record_account(is_cheap2,buy_amount3):
  account = is_cheap2 * buy_amount3

  print "麻麻在 小本子上记了买菜花销%s元  " %(account)

def talk_with_daddy(is_cheap3, buy_amount3):
  if is_cheap3:
  	print '老妈回到家，跟老爸说：“今天价格不贵，买了%s斤”。 ' %(buy_amount3)
  else:
  	print '老妈回到家里，跟老爸说“今天去买菜，菜好贵额，没买"。 '

def buybuybuy():
  good_price =6 #每降低一元，多买一斤
  reasonalbe_price = 5
  buy_amount = 2 #每降低一元，多买一斤

  who = '大蒜的麻麻 '
  good_description = "西双版纳大白菜 "

  is_cheap = False 

  print "%s 上街看到了%s,卖%s元/斤  " %(who, good_description, good_price)

  if good_price <= reasonalbe_price :
  	print '她认为便宜 '
  	is_cheap = True
  	#解决老妈买几斤
  	#5-2 4-3 2-4
  	buy_amount = 2 + (reasonalbe_price -good_price)
  	if buy_amount > 4:
  	  buy_amount =4

  	print '她买了%d斤 ' % (buy_amount)
  else:
  	print '她认为贵了 '
  	is_cheap = False
  	print '她并没有买，扬长而去 '

  return is_cheap, buy_amount 

def main():
  #买买买
  is_cheap2,buy_amount3 = buybuybuy()
  #说说说
  talk_with_daddy(is_cheap2,buy_amount3)
  #记记记
  record_account(is_cheap2,buy_amount3)

if __name__  == '__main__':
  main()
  
#我眼中的单一职责原则是，一个函数只执行一种运行能力，实现一个目标。例如：买买买函数，就只实现买买买而不执行记记记