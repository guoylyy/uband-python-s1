#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Tingting

def buybuybuy():
    who = '亭亭的妈妈'
    good_description = "西双版纳大白菜"
  
    reasonable_price = 6
    buy_amount = 2 
    good_price = 1
 
    is_cheap = False
   
    cost = 0
   
    print "%s上街看到了%s, 卖 %d元/斤" % (who, good_description, good_price)
  
    if good_price <= reasonable_price:
        print '她认为便宜'
        is_cheap = True
        buy_amount = 2 + (reasonable_price - good_price)
        if buy_amount > 4:
            buy_amount = 4
            print '她买了 %d 斤' % (buy_amount)
            cost = buy_amount * good_price 
        else: 
            print '她认为贵了 '
            is_cheap = False
            print '她并没有买，扬长而去'
    return is_cheap, buy_amount, cost, good_description

def talk_with_daddy(is_cheap, buy_amount):
    if is_cheap:
        print '妈妈回到家里,跟爸爸说:"今天去买菜,价格不贵,买了 %d 斤"' % (buy_amount)
    else:
        print '妈妈回到家里,跟爸爸说:"今天去买菜,菜好贵额,没买"'

def record(good_description, cost):
    if cost > 0:
        print '老妈在记账本上记今天买了%s,花了%d元' % (good_description, cost)
    else:
        pass
    
def main():
    is_cheap, buy_amount, cost, good_description = buybuybuy()
    talk_with_daddy(is_cheap, buy_amount) 
    record(good_description, cost)
    
if __name__ == '__main__':
    main() 