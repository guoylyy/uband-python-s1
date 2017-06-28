#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: yanyan

def main():
  who='my mom'
  good_price= 6
  good_description= 'cabbages'

  is_cheap= False
  reasonable_price= 5
  buy_amount= 2

  print '%s saw %s on the street, which sold for %dRMB half of kilo' % (who,good_description,good_price)
  if good_price<=reasonable_price:
    print 'she thinks it cheap'
    is_cheap= True
    buy_amount= 2+ (reasonable_price- good_price)
    if buy_amount>4:
    	buy_amount=4
    print 'she bought %d '% (buy_amount)
  else:
    print 'she thinks it expensive'
    is_cheap= False
    print 'she did not purchase it, she left instead'

if __name__ == '__main__':
  main()