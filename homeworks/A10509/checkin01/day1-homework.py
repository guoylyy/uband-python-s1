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
  who = "卤蛋mum"
  good_price = 2
  reasonable_price = 5
  buy_amount = 2
  food = "胡萝卜"
  is_cheap = False

  
  print "%s上街看到%s %d一斤" %(who, food, good_price)

  if good_price <= reasonable_price:
  	  
     buy_amount = buy_amount + reasonable_price - good_price
     if buy_amount > 4:
        buy_amount = 4
     print "表示来%d斤" %(buy_amount)
     is_cheap = True 
  else:
     print "她觉得贵，扬长而去" 


if __name__ == '__main__':
  main()

