#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: zi le

# 1. 对照锅蜀黍的代码自己打一遍
# 2. 把锅蜀黍的老板改成你老妈，跑通
# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
# 6. xxx 还有两天的作业明天和后天放出来，属于阅读理解 + 练习深化
#   （ps：第 5 题错了也没关系，提交上来过后我会讲评）
def main():
	who='梓乐的妈妈'
	good_description="西双版纳大白菜 "

	is_cheap=False

	good_price=3.5#题3，这里的商品价格改为<=5的数字
	reasonable_price=5#题3，这里的接受价格改为>=6的数字。
	buy_amount=2

	print "%s上街看到了%s,卖%0.2f元/斤 "%(who,good_description,good_price)
	#题4，if就是一个条件语句，提供一个标准，如果满足该标准就如何如何。<=和>=感觉是对比语句，用于对前后数据的大小对比。
	if good_price<=reasonable_price:
		print '她认为便宜 '
		is_cheap=True
		#题5
		if reasonable_price-1<good_price<=reasonable_price:
			print '她买了%d斤 '%(buy_amount)
		if reasonable_price-2<good_price<=reasonable_price-1:
			print '她买了%d斤 '%(buy_amount+1)
		if good_price<=reasonable_price-2:
			print '她买了%d斤 '%(buy_amount+2)
	else:
		print '她认为贵了 '
		is_cheap=False
		print '她并没有买，扬长而去 '


if __name__ == '__main__':
  main()
