#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Mansur
#1. 对照锅蜀黍的代码自己打一遍
def main():
  who = '锅蜀黍的老妈'
  good_price = 6
  good_description = "西双版纳大白菜"

  is_cheap = False 
  reasonable_price = 12
  buy_amount = 2 

  print "q1. 对照锅蜀黍的代码自己打一遍"
  print "%s上街看到了%s,卖 %d 每斤" % (who,good_description,good_price)

  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    print '她买了 %d 斤' % (buy_amount)
  
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'

if __name__ == '__main__':
  main()

# 2. 把锅蜀黍的老板改成你老妈，跑通
def main():
  who="老妈"
  good_price=6
  good_description="大白菜"

  is_cheap=False
  reasonable_price=5
  buy_amount=2

  print "q2.把锅蜀黍的老板改成你老妈，跑通"
  print "%s上街看到了%s,卖%d每斤"%(who,good_description,good_price)

  if good_price>reasonable_price:
    print "认为贵了"
    is_cheap=False
    print "没有买，扬长而去"
  else: 
    print"认为便宜"
    is_cheap=True
    print"买了%d斤"%(buy_amount)

if __name__ == '__main__':
  main()

# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
def main():
  who="老妈"
  good_price=6
  good_description="大白菜"

  is_cheap=False
  reasonable_price=5
  buy_amount=2

  print "q3.把锅蜀黍的老板改成你老妈，跑通"
  print "%s上街看到了%s,卖%d每斤"%(who,good_description,good_price)

  if good_price>reasonable_price:
    print "认为贵了"
    is_cheap=False
    # print "没有买，扬长而去" 
    print "只买了%d斤"%(buy_amount)  #改动
  else: 
    print"认为便宜"
    is_cheap=True
    print"买了%d斤"%(buy_amount)

if __name__ == '__main__':
  main()

# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
# 回答下面几个问题
# 1）. what's the meaning of 'number', 'string', 'boolean' in python? 

# 2）. try to describe the meaning of 'if' statement in your mind?

# 3）. Why we need > < ==  >= <= ...etc...?

# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
def main():
  who="老妈"
  good_price=6
  good_description="大白菜"

  is_cheap=False
  reasonable_price=5
  buy_amount=2

  print "%s上街看到了%s,卖%d每斤"%(who,good_description,good_price)

  if good_price>reasonable_price:
    print "认为贵了"
    is_cheap=False
    print "没有买，扬长而去" 
  else: 
    
    print"认为便宜"
    is_cheap=True
    print"买了%d斤"%(buy_amount)

if __name__ == '__main__':
  main()

