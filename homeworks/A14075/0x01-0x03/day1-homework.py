#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: hydewww (not good at English)

# 思考题
# 1. number：数值    string：字符串（即引号内的） boolean：布尔类型，分为True/False
# 2. if judgement: 判断为True时运行缩进中的语句块 否则运行else（可无）
# 3. 明确了True/False的判断，减少因自然语言产生的模棱两可的答案。

def main():
  who = 'Mom'
  good_price = 2
  good_description = "Nice Cabbage"

  is_cheap = False
  reasonable_price = 5 # highest price

  #new variable
  buy_min_amount = 2 # least amount
  buy_max_amount = 4 #
  buy_amount = 0

  print ('%s saw "%s" sold at %d yuan per catty when shopping. ' % (who, good_description, good_price)  )

  if good_price <= reasonable_price:
    print ('She thought it was cheap.')
    is_cheap = True
    # Q5 solution --  随价格/最大最小购买数改变
    buy_amount = buy_min_amount + reasonable_price - good_price
    if buy_amount > buy_max_amount :
        buy_amount = buy_max_amount
    # Q5 over
    print ('She bought %d catty' % (buy_amount) )
  else:
    print ('She thought it was expensive. ')
    is_cheap = False
    print ("She didn't buy it. ")

if __name__ == '__main__':
  main()
