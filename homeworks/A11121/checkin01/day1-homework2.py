#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Jinxiao
# 1. 对照锅蜀黍的代码自己打一遍
# 2. 把锅蜀黍的老板改成你老妈，跑通
def main():
	who = '小金人的老妈'
	good_price = 6 #小贩的价格
	good_description = '西双版纳大白菜' #小贩的招牌

	is_cheap = False #是否便宜
	reasonable_price = 5 #老妈觉得合适的价格
	buy_amount = 2 #准备买2斤
	#开始表演
	print '作业1 2题'
	print '%s上街看到了%s,卖%d元/斤'% (who, good_description, good_price)
	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		print '她买了%d斤' % (buy_amount)
	else:
		print '她认为贵'
		is_cheap = False
		print '她并没有买,扬长而去'

# run function
if __name__ == '__main__':
  main()


# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
# 第一种修改，修改老妈觉得合适的价格
def main():
	who = '小金人的老妈'
	good_price = 6 #小贩的价格
	good_description = '西双版纳大白菜' #小贩的招牌

	is_cheap = False #是否便宜
	reasonable_price = 6 #老妈觉得合适的价格，第一种修改，5改为6
	buy_amount = 2 #准备买2斤
	#开始表演
	print '作业第3题第1处'
	print '%s上街看到了%s,卖%d元/斤'% (who, good_description, good_price)
	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		print '她买了%d斤' % (buy_amount)
	else:
		print '她认为贵'
		is_cheap = False
		print '她并没有买,扬长而去'	

# run function
if __name__ == '__main__':
  main()

# 第二种修改，修改小贩的价格
  def main():
	who = '小金人的老妈'
	good_price = 4 #小贩的价格
	good_description = '西双版纳大白菜' #小贩的招牌

	is_cheap = False #是否便宜
	reasonable_price = 5 #老妈觉得合适的价格
	buy_amount = 2 #准备买2斤
	#开始表演
	print '作业第3题第2处'
	print '%s上街看到了%s,卖%d元/斤'% (who, good_description, good_price)
	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		print '她买了%d斤' % (buy_amount)
	else:
		print '她认为贵'
		is_cheap = False
		print '她并没有买,扬长而去'	

# run function
if __name__ == '__main__':
  main()

  # 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
  #  1. what's the meaning of 'number', 'string', 'boolean' in python? 
  # number 数字 可以进行计算；
  # string 字符串 通常在引号内，字符信息，不会作为变量或数字运算，常常是文字信息  
  # boolean 是一种数据类型 可以对相应的变量进行赋值，但只能是True or False 两种形式。

  #2. try to describe the meaning of 'if' statement in your mind?
  #条件语句，如果符合。。。执行xxx，否则执行xxx

  #3. Why we need > < ==  >= <= ...etc...?
  #对满足条件的形式进行量化规定，帮助更好的执行意愿。


  # 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
  def main():
	who = '小金人的老妈'
	good_price = 2 #小贩的价格 每便宜1元，多买1斤
	good_description = '西双版纳大白菜' #小贩的招牌

	is_cheap = False #是否便宜
	reasonable_price = 5 #老妈觉得合适的价格
	buy_amount = 2 #准备买2斤,每便宜1元，多买1斤，最多买4斤
	#开始表演
	print '作业第5题'
	print '%s上街看到了%s,卖%d元/斤'% (who, good_description, good_price)
	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount = buy_amount + reasonable_price - good_price
		if buy_amount > 4:
			buy_amount = 4
		print '她买了%d斤'% (buy_amount)
	else:
		print '她认为贵'
		is_cheap = False
		print '她并没有买,扬长而去'

# run function
if __name__ == '__main__':
  main()
