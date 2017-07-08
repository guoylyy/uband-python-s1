#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 1. 对照锅蜀黍的代码自己打一遍
# 2. 把锅蜀黍的老板改成你老妈，跑通
# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
# 6. xxx 还有两天的作业明天和后天放出来，属于阅读理解 + 练习深化
#   （ps：第 5 题错了也没关系，提交上来过后我会讲评）
def main():
  who = 'Mom'
  good_price = 6 #there could be the same price or price under the reasonable_price
  good_description = "peanuts"

  is_cheap = False
  reasonable_price = 5 #there could be the same price or higher price than the good_price
  buy_amount = 2
  print "%s saw %s was sold at %d /kg on the street" % (who, good_description, good_price)

  if good_price >= reasonable_price: #change the greater-than to the less-than
  	print 'She thought that is cheap'
  	is_cheap = True
  	print 'She bought %d kilogram' % (buy_amount)
  else:
  	print "She thought that's expensive"
  	is_cheap = False
  	print 'She went away without buying anything'

if __name__ == '__main__':
  main()
