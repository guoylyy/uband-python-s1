#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yanyan
def talk_with_daddy(is_cheap3,buy_amount3):
  if is_cheap3:
    print 'she told my dad :"today the cabbages are cheap, so I bought %d"'%(buy_amount3)
  else:
    print 'she told my dad:"today the cabbages are expensive, I did not buy any"'


  

def record_account(is_cheap4,total_cost):
  if is_cheap4:
    print ' my mon recorded how much she spent, %d yuan'%(total_cost)
  else:
    print 'mom didnt spend any money on vegetables.'

def buybuybuy():
  who='my mom'
  good_price= 4
  good_description= 'cabbages'

  is_cheap= False
  reasonable_price= 5
  buy_amount= 2
  total_cost=(2 +(reasonable_price- good_price))*good_price
  
  print '%s saw %s on the street, which sold for %dRMB half of kilo' % (who,good_description,good_price)
  if good_price<=reasonable_price:
    print 'she thinks it cheap'
    is_cheap= True
    buy_amount= 2+ (reasonable_price - good_price)
    if buy_amount>4:
      buy_amount=4
    print 'she bought %d'% (buy_amount)
    print 'she spent %d '% (total_cost)
  else:
    print 'she thinks it expensive'
    is_cheap= False
    print 'she did not purchase it, she left instead'
  

  return is_cheap,buy_amount,total_cost


def main():
  is_cheap2,buy_amount2,total_cost = buybuybuy()
  talk_with_daddy(is_cheap2,buy_amount2)
  record_account(is_cheap2, total_cost)
  

if __name__ == '__main__':
  main()

 
 

  #单一职责就是一个区域块只干一件事，只干一件事