#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: June


def main():
  who = 'June'
  good_price=6
  good_description= "cabbige"

  is_cheap = False 
  reasonable_price = 4
  buy_amount = 2
  discount = reasonable_price - good_price #价差
  biggest_discount = 2 # 最大的价差

  print "%ssee %s,sell %syuan/500g" % (who, good_description, good_price)
  if good_price <= reasonable_price:
    print 'she thinks it is cheap'
    is_cheap = True
    if discount <= biggest_discount :
      buy_amount = 4/2
      print 'she buy %d kg' %(buy_amount)
    else:
      buy_amount=(buy_amount+ discount)/2
      print'shebuy %d kg'%(buy_amount)
  else:
    print 'she thinks it is expansive'
    is_cheap = False
    print 'she does no buy but leave' 

if __name__ == '__main__':
  main()