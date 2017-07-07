#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: qianchang

# 单一职责原则: one thing at a time
 
def buy():
    who = "浅唱的老妈"
    good_description = "西双版纳大白菜"
    good_price = 3
    resonable_price = 5
    buy_amount = 2
    is_cheap= True
    
    print "%s上街看到了%s，卖%d元一斤。" % (who, good_description, good_price)
    if good_price <= resonable_price:
        is_cheap= True
        buy_amount = buy_amount + resonable_price - good_price
        if buy_amount >= 4:
            buy_amount = 4
        print "她认为便宜，买了%d斤。" % (buy_amount)
    else:
        is_cheap= False
        print "她认为贵了，她没有买扬长而去"
    return is_cheap, buy_amount, good_price

def tell(is_cheap, buy_amount):
    if is_cheap:
        print '老妈对老爸说: "今天白菜便宜，买了%d斤。"' % (buy_amount)
    else:
        print '老妈对老爸说，"今天白菜贵，没买。"'

def record(is_cheap, buy_amount, good_price):
    if is_cheap:
        total_price = buy_amount * good_price
        print "老妈记账：买了%d斤白菜，%d元一斤，共花了%d元。" % (buy_amount, good_price, total_price)
    else:
        pass
    
def main():
    is_cheap, buy_amount, good_price = buy()
    tell(is_cheap, buy_amount) 
    record(is_cheap, buy_amount, good_price)

if __name__ == '__main__':
    main()
 