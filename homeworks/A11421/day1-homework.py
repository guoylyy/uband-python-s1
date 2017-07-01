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
  
  who = '锅蜀黍'
  good_price = 600
  good_name = '内蒙古炭烤羊腿'
  
  cheap = 1000
  # is_cheap = True
  buy_amount = 2 

  print "%s在街上看到了%s， 售价¥%d／只" % (who, good_name, good_price)

  if good_price <= cheap:
  	buy_amount = buy_amount + (cheap - good_price)/100
  	if buy_amount <= 4:
  		pass
  	else:
  		buy_amount =4
  	print "他认为便宜，买了 %d 只" % (buy_amount)
  else:
  	print "他认为贵，扬长而去"

if __name__ == '__main__':
  main()
