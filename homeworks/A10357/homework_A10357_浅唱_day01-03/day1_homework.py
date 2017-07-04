#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: qianchang

#思考题
#1.what are "number", "string" and "boolean" in python seperately?
    #The numeric data type refers to data such as integers, floats and so on.
    #Strings refer to text data types such letters, digits, punctuation marks, etc.
    #The Boolean data has only two possible values: true or false.
#2.try to describe the meaning of 'if' statement
    #If 'if' is true, then do the following statement, otherwise do the opposite.
#3.Why we need > < == >= <= ...etc...?
    #Because we need to tell our computers what to do under what condition.

def main():
    who = '浅唱的老妈'
    good_price = 4
    good_description = '西双版纳大白菜'
    is_cheap = False
    resonable_price = 5
    buy_amount = 2
    
    print "%s上街看到了%s，卖%d元一公斤" % (who, good_description, good_price)
    if good_price <= resonable_price:
        print '她认为便宜'
        is_cheap = True
        buy_amount = 2 + (resonable_price - good_price)
        if buy_amount >= 4:
            buy_amount = 4 
        print "她买了%d斤" % (buy_amount)
    else:
        print "她认为贵了"
        is_cheap = False
        print "她并没有买，扬长而去"

# run function
if __name__ == '__main__':
 	main()