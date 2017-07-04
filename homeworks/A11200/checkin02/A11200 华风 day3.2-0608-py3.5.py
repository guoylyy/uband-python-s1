# -*- coding: utf-8 -*-
# @author: Huafeng

# 妈妈记账
# 
def sum(is_cheap4, good_price2, buy_amount3):
   if is_cheap4:
     total_amount = buy_amount3 * good_price2

     print ('老妈在小本子上记账，花了 %d 元。' % (total_amount))
     
def talk_with_dad(is_cheap3, buy_amount3):
  if is_cheap3:
    print ('老妈回到家里，跟老爸说:“今天去买菜，价格不贵，买了 %d 斤”。' %(buy_amount3))
  else:
    print ('老妈回到家里，跟老爸说:"今天去买菜，菜好贵额，没买"。')

def buybuybuy():
  good_price = 4 
  reasonable_price = 5
  buy_amount = 2

  who = '华风的老妈'
  good_description = '西双版纳大白菜'

  is_cheap = False

  print ('%s上街看到了%s，卖 %d 元/斤' % (who, good_description, good_price))

  if good_price <= reasonable_price:
    print ('她认为便宜')
    is_cheap = True
    
    buy_amount = 2 + (reasonable_price - good_price)

    if buy_amount > 4:
      buy_amount = 4
      print ('她买了 %d 斤' % (buy_amount))

  else:
    print ('她认为贵了 ')
    is_cheap = False
    print ('她并没有买，扬长而去')


  return is_cheap, buy_amount, good_price

def main():

  is_cheap2, buy_amount2,good_rice2 = buybuybuy ()

  talk_with_dad (is_cheap2, buy_amount2 )  
  # 记账
  sum (is_cheap2,good_rice2,buy_amount2)

if __name__ == '__main__':
  main()
