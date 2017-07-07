#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Betty

# 1. 对照锅蜀黍的代码自己打一遍
def main():
  who = '锅蜀黍的老妈'
  good_price = 6 #小贩的价格
  good_description = '西双版纳大白菜' #小贩的招牌

  is_cheap = False #是否便宜
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤

  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

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
  who = 'Betty的老妈'
  good_price = 6 #小贩的价格
  good_description = '西双版纳白菜' #小贩的招牌

  is_cheap = False #是否便宜
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤

  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

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

# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
def main():
  who = 'Betty的老妈'
  good_price = 6 #小贩的价格
  good_description = '西双版纳大白菜' #小贩的招牌

  is_cheap = False #是否便宜
  reasonable_price = 7 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤

  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  if good_price <= reasonable_price:
  	print '她认为便宜'
  	is_cheap = True
  	print '她买了 %d 斤' % (buy_amount)
  else:
  	print '她认为贵了 '
  	is_cheap = False
  	print '她并没有买，扬长而去'

#如何使老妈买白菜：
#1.使小贩菜价变低
#2.使老妈能接受的菜价变高
#3.不考虑价格高低，目标是看到就买

if __name__ == '__main__':
  main()

# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
#1. what's the meaning of 'number', 'string', 'boolean' in python? 
#   在我的理解里，number就是数字，string字符串，用英文引号框起来的，字符串里面可以打字。boolean只有True和False，有and、or与not三种关系，一般用来判断的，经常用在if语句里。
#2. try to describe the meaning of 'if' statement in your mind?
#   if语句就像是分了很多叉的树杈，一步步走下去，如果A就B，如果不A就C，情况越复杂if语句就越复杂。
#3. Why we need > < ==  >= <= ...etc...?
#   因为要确定范围。

# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
def main():
  who = 'Betty的老妈'
  good_price = 4 #小贩的价格
  good_description = '西双版纳大白菜' #小贩的招牌

  is_cheap = False #是否便宜
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤

  price_minus = reasonable_price - good_price
  buy_amount = buy_amount + price_minus
  max_amount = 4 #最多买 4 斤

  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  if good_price <= reasonable_price:
    print '她认为便宜'
    if buy_amount <= max_amount:
      is_cheap = True
      print '她买了 %d 斤' % (buy_amount)
    else:
      print '她买了 %d 斤' % (max_amount) 
    
  else:
  	print '她认为贵了 '
  	is_cheap = False
  	print '她并没有买，扬长而去'


if __name__ == '__main__':
  main()

# 6. xxx 还有两天的作业明天和后天放出来，属于阅读理解 + 练习深化
#   （ps：第 5 题错了也没关系，提交上来过后我会讲评）
def main():
  pass

if __name__ == '__main__':
  main()
