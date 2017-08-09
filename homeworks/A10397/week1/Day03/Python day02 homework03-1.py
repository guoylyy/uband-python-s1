#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tangxiaocu

def talk_with_daddy(is_cheap3, buy_amount3):
  if is_cheap3:
    print '老妈回到家里，跟老爸说：“今天去买菜，价格不贵，买了两斤。”' %(buy_amount3)
  else:
    print '老妈回到家里，跟老爸说：“今天去买菜，菜好贵啊，就没买。”'

def buybuybuy():
  who = '糖小醋的老妈 '
  good_description = "西双版纳大白菜" 

  is_cheap = False 

  good_price = 6 #每降低一元，多买一斤
  reasonable_price = 5 
  buy_amount = 2 #每降低一元，多买一斤

  print '%s上街看到了%s, 卖 %d 元/斤' % (who, good_description, good_price)

  if good_price <= reasonable_price:
	 print '她认为便宜'
	 is_cheap = True
	 buy_amount = (reasonable_price - good_price)+2
   #解决老妈买几斤的问题
   #5-2 4-3 3-4 2-4
	 if buy_amount >= 4:
	  print '她买了 4 斤' 
	 else :
		print '她买了 %d 斤' % (buy_amount)
  else:
   print '她认为贵了'
   is_cheap = False
   print '她并没有买，扬长而去'

  return is_cheap, buy_amount

def main():
  is_cheap2, buy_amount2 = buybuybuy()
  talk_with_daddy(is_cheap2, buy_amount2)


#show time
if __name__ == '__main__':
  main()
