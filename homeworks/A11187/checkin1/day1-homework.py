#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xiangrikui

# 1. 对照锅蜀黍的代码自己打一遍
# 2. 把锅蜀黍的老板改成你老妈，跑通
# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
# 6. xxx 还有两天的作业明天和后天放出来，属于阅读理解 + 练习深化
#   （ps：第 5 题错了也没关系，提交上来过后我会讲评）
def main():
	reasonable_price = 5
	good_price = 3  #题3. 改变小贩的价格，使之低于5元，就可以走if后面的函数段，而不是else后面的部分，e.g. 4.5
	buy_amount = 2 #准备买 2 斤
	
	who = 'xiangrikui的妈妈 '
	good_description = "西双版纳大白菜" #小贩的招牌

	is_cheap = False #是否便宜
	
	print "%s上街看到了%s，卖 %0.2f 元/斤 " % (who, good_description, good_price)
	# 题4.if语句用来判断检验，比如说满足逻辑中的真值运算，就运行if后的语句，反之则运算else后的语句；； <= >= 等符号是进行比较的运算符就像在数学中的运算
	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		#解决妈妈购买白菜的数目问题
		buy_amount = 2 + (reasonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'

if __name__ == '__main__':
	main()
