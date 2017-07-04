#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: shangxindepidan

# 1. 对照锅蜀黍的代码自己打一遍
print '#1'
def main():		
	who = '锅蜀黍的老妈'
	good_price = 6 #小贩的价格
	good_description = "西双版纳的大白菜" #小贩的招牌

	is_cheap = True #是否便宜
	reasonable_price = 5 #老妈能接受的最高价格
	buy_amount = 2 #准备买 2 斤

	print "%s上街看到了%s, 卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去'	

if __name__ == '__main__':
	main()


# 2. 把锅蜀黍的老板改成你老妈，跑通
print '#2'
def main():
	who = '伤心的皮蛋的老妈'
	good_price = 6
	good_description = "西双版纳的大白菜"
	is_cheap = True
	reasonable_price = 5
	buy_amount = 2

	print "%s上街看到了%s, 卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去'
if __name__ == '__main__':
	main()


# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
print '#3-1'
def main():
	who = '伤心的皮蛋的老妈'
	good_price = 5 #修改小贩的价格
	good_description = "西双版纳的大白菜"
	is_cheap = True
	reasonable_price = 5
	buy_amount = 2

	print "%s上街看到了%s, 卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去'
if __name__ == '__main__':
	main()

print '#3-2'
def main():
	who = '伤心的皮蛋的老妈'
	good_price = 6
	good_description = "西双版纳的大白菜"
	is_cheap = True
	reasonable_price = 6 #修改老妈能接受的最高价格
	buy_amount = 2

	print "%s上街看到了%s, 卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去'
if __name__ == '__main__':
	main()


# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
print '#4'
print "1. what's the meaning of 'number', 'string', 'boolean' in python?"
print "A: Number means figures like 1, 2, 3, etc. String stands for letters or combination of letters and numbers. Boolean is an expression to define if one condition is true or false."
print "2. try to describe the meaning of 'if' statement in your mind?"
print "A: 'If' statement is a way to help decide what to do under two or more different random conditions."
print "3. Why we need > < ==  >= <= ...etc...?"
print "A: Because we need to compare variables with some certain values or other variables to complete an 'if' statement, and help define a random condition."

# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
print '#5-1'
def main():
	who = '伤心的皮蛋的老妈'
	good_price = 5
	good_description = "西双版纳的大白菜"
	is_cheap = True 
	reasonable_price = 5 
	buy_amount = 2

	print "%s上街看到了%s, 卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		is_cheap = True
		print "她认为便宜，打算买 %d 斤" % (buy_amount)
		while buy_amount < 4: 
			good_price = good_price - 1
			buy_amount = buy_amount + 1
			print "如果每斤价格再低 1 元，卖 %d 元/斤，那么她会再多买一斤，即 %d 斤" % (good_price, buy_amount)
		while good_price > 0:
			good_price = good_price - 1
			buy_amount=4
			print "如果每斤价格再低 1 元，卖 %d 元/斤，那么她会再多买一斤，即 %d 斤" % (good_price, buy_amount)
	else: 
		is_cheap = False
		print "她认为贵了，并没有买，扬长而去"
if __name__ == '__main__':
	main()

print '#5-2'
def main():
	who = '伤心的皮蛋的老妈'
	good_price = 0
	good_description = "西双版纳的大白菜"
	is_cheap = True 
	reasonable_price = 5 
	buy_amount = 2

	print "%s上街看到了%s, 卖 %d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜 '
		is_cheap = True
		buy_amount = 2 + (reasonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了 %d 斤 ' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去'
if __name__ == '__main__':
	main()

# 6. xxx 还有两天的作业明天和后天放出来，属于阅读理解 + 练习深化
#   （ps：第 5 题错了也没关系，提交上来过后我会讲评）
