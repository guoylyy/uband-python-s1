# -*- coding: utf-8 -*-

def talk(is_cheap, buy_amount):
  if is_cheap:
    print 'Mom tells dad, "the veg price is reasonable and she buys %d grams."' %(buy_amount)

  else:
    print ' Mom tells dad, "the veg price is too expensicve to buy so she leaves."'

def diary(is_cheap, buy_amount):
  if is_cheap:
    print 'Mom wirtes at her diary, "the veg price is reasonable and she buys %d grams."' %(buy_amount)

  else:
    print ' Mom wirtes at her diary, "the veg price is too expensicve to buy so she leaves."'

def buy():
  who = 'Mom'
  good_description = "vegetable"

  good_price = -1  
  reasonable_price = 5 
  is_cheap = False 
  buy_amount = 2 + reasonable_price - good_price

  print "%s sees %s sold at %d dollars per gram." % (who, good_description, good_price)
  if good_price <= reasonable_price:
    is_cheap = True
    if buy_amount > 4:
    	buy_amount = 4
    print 'She thinks the price is reasonable and she would like to buy %d grams.' % (buy_amount)
 
  else: 
    is_cheap = False
    print 'She thinks it is too expensicve to buy so she leaves.'

  return is_cheap, buy_amount





if __name__ == '__main__':
	is_cheap, buy_amount = buy()
 	talk(is_cheap, buy_amount)
 	diary(is_cheap, buy_amount)
