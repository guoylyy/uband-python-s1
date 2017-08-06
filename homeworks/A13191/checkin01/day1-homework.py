#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Chauncey

# 1. 对照锅蜀黍的代码自己打一遍
# 2. 把锅蜀黍的老板改成你老妈，跑通
# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
# 6. 还有两天的作业明天和后天放出来，属于阅读理解 + 练习深化
#   （ps：第 5 题错了也没关系，提交上来过后我会讲评）
def main():
	who = 'Chauncey的老妈 '
	good_price = 3
	good_description = '西双版纳大白菜'

	is_cheap = False
	reasonable_price = 5
	buy_amount = 2

	print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		if good_price == 3:
			buy_amount = buy_amount + 1
		if good_price == 2:
			buy_amount = buy_amount + 2
		print '她买了%d斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'

	

if __name__ == '__main__':
  main()

# 1. number就是数字，string是字符串，boolean是true or false
# 2. if就是判断，满足某一个条件的时候执行下面一段代码，否则不执行
# 3. 因为需要比较数值，所以需要<, <=, >, >=, ==等等