#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: 园子

# 1. 对照锅蜀黍的代码自己打一遍
# 2. 把锅蜀黍的老板改成你老妈，跑通
# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
# 6. xxx 还有两天的作业明天和后天放出来，属于阅读理解 + 练习深化
#   （ps：第 5 题错了也没关系，提交上来过后我会讲评）
def main():
  who = '园子的麻麻'
  good_price = 6 
  good_description = "西双版纳大白菜"

  is_cheap = False
  reseanable_price = 5
  buy_amount = 2 

  print "%s上街看到了%s, 卖 %d 元/斤" % (who, good_description, good_price)

  if good_price <= reseanable_price:
    print '她认为便宜'
    is_cheap = True
    print '她买了 %d 斤' % (buy_amount)
  else:
    print '她认为贵了'
    is_cheap = False
    print '她并没有买，扬长而去'


if __name__ == '__main__':
  main()


  #思考题  
  #number是数；string是字符串是字符的序列，就是一组单词，要使用引号
  #number和string这两个都是具有字面上意义的常量 
  #boolean是布尔值用于判断
  #if是一个条件语句通过True或False执行指令
  # < > = <= >= 这些都是对数值进行运算的运算符
