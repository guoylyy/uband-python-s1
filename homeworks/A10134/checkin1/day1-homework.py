#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Liluo

# 1. 对照锅蜀黍的代码自己打一遍
# 2. 把锅蜀黍的老板改成你老妈，跑通
# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
#1.修改good_price; 2.修改reasonable_price;3.修改if..else的条件（尝试一个）

# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
#1. what's the meaning of 'number', 'string', 'boolean' in python? 
#number: numeric values(integer, float)
#boolean:true=1,false=0
#string：a contiguous set of characters represented in the quotation marks
#2. try to describe the meaning of 'if' statement in your mind?
#judge the result and determine which steps 
#3. Why we need > < ==  >= <= ...etc...?
#to compare the number

# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
# 6. xxx 还有两天的作业明天和后天放出来，属于阅读理解 + 练习深化
#   （ps：第 5 题错了也没关系，提交上来过后我会讲评）
def main():
	who="Liluo's mom "
	good_price=3.9
	good_description="西双版纳大白菜 "

	is_cheap=False
	reasonalbe_price=5
	buy_amount=2

	print "%s上街看到了%s,卖%0.2f元/斤"%(who,good_description,good_price)

	if good_price<=reasonalbe_price:
		print '她认为便宜'
		is_cheap=True
		buy_amount=2+(reasonalbe_price-good_price)
		if buy_amount>4:
			buy_amount=4
		print '她买了%0.2f斤'%(buy_amount)
	else:
		print '她认为贵了'
		is_cheap=False
		print '她并没有买，扬长而去'

if __name__ == '__main__':
  main()
