#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Pennsylvania

# 1. 对照锅蜀黍的代码自己打一遍
# 2. 把锅蜀黍的老板改成你老妈，跑通
# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
# 6. xxx 还有两天的作业明天和后天放出来，属于阅读理解 + 练习深化
#   （ps：第 5 题错了也没关系，提交上来过后我会讲评）

# For beginner
# 1. variable - num,str,boolean
# 2. if
# 3. > < >= <= == 
# 4. print
def main():
  who = "Pennsylvania的老妈"
  good_description = "西双版纳大白菜"

  good_price = 2
  reasonable_price = 5
  buy_amount = 2
  

  is_cheap = False

  print "%s上街看到了%s, 卖 %d 元/斤" % (who, good_description, good_price)
  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    buy_amount = 2 + (reasonable_price - good_price)
    if buy_amount > 4:
      buy_amount = 4
    print '她买了 %d 斤' % (buy_amount) #试了N遍都显示缩进错误，肉眼实在看不出差别...万般无奈下直接copy了蜀黍sample code中的这句话，结果总算对了
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'
 


 # run function 	
if __name__ == '__main__':
  main()

# 若要让老妈买2斤白菜，将good_price处的价格改为5，或5以下的数字就好
# 我认为变量指：在给定条件下，会引起输出结果不同的变化的数值
# if指：条件语句中表示某一条件 就是“如果在这种情况下”，会得到怎样的结果
# <= >=指：条件语句中某一变量与给定数值间的大小关系
