#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Janice

# 1. 对照锅蜀黍的代码自己打一遍
# 2. 把锅蜀黍的老板改成你老妈，跑通
# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
	#01-修改good_price或者resonable_price的值，使得前者小于后者
	#02-举例（1）good_price=4；（2）resonable_price=7
# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
	# if 表示判断，如果后面的条件成立，则执行相应语句，否则跳过
	# <= 小于等于，用于判断，若前面的小于后面，则返回True，否则返回False
	# >= 大于等于，同上
# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
	#
# 6. xxx 还有两天的作业明天和后天放出来，属于阅读理解 + 练习深化
#   （ps：第 5 题错了也没关系，提交上来过后我会讲评）
def main():
	who = '清蒸的妈妈'
	good_description = "瓜州大白菜"
	

	good_price = 6 #商品价格
	resonable_price = 5
	buy_amount = 2

	is_cheap = False 

	#开始表演
	print "%s上街看到了%s ,卖 %d 元/斤" % (who, good_description, good_price)

	if  good_price <= resonable_price:
		print '她认为便宜'
		is_cheap = True
		#加分题
		buy_amount = buy_amount + (resonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print ' 她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去 '

if __name__ == '__main__':
  main()
