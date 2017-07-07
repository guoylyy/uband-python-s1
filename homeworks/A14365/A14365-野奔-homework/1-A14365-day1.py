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
#def main():
 # pass

#if __name__ == '__main__':
#  main()

# 作业1：敲一遍代码
def main():
 who = '郭叔叔的老妈'
 good_price = 6  #小贩的价格
 good_description = "西双版纳大白菜" #小贩的招牌

 is_cheap = False #是否便宜
 reasonable_price = 5 #老妈能接受的最高价格
 buy_amount = 2 #准备买2斤


 #开始你的表演
 #go 我们来走一组
 print "%s上街看到了%s,卖%d元/斤" % (who,good_description,good_price)

 if good_price <= reasonable_price:
 	print '她认为便宜'
 	is_cheap = True
 	print '她买了%d斤' % (buy_amount)
 else:
 	print '她认为贵了'
 	is_cheap = False
 	print '她并没有买，扬长而去'

if __name__ == '__main__':
	main()

# 作业2：改名字

def main():
 who = '艾妈妈'
 good_price = 6  #小贩的价格
 good_description = "小青菜" #小贩的招牌

 is_cheap = False #是否便宜
 reasonable_price = 5 #老妈能接受的最高价格
 buy_amount = 2 #准备买2斤


 #开始你的表演
 #go 我们来走一组
 print "%s上街看到了%s,卖%d元/斤" % (who,good_description,good_price)

 if good_price <= reasonable_price:
 	print '她认为便宜'
 	is_cheap = True
 	print '她买了%d斤' % (buy_amount)
 else:
 	print '她认为贵了'
 	is_cheap = False
 	print '她并没有买，扬长而去'

if __name__ == '__main__':
	main()

#作业3
#1.可以修改good_price,reasonable_price
def main():
 who = '艾妈妈'
 good_price = 6  #小贩的价格
 good_description = "小青菜" #小贩的招牌

 is_cheap = False #是否便宜
 reasonable_price = 7 #老妈能接受的最高价格
 buy_amount = 2 #准备买2斤


 #开始你的表演
 #go 我们来走一组
 print "%s上街看到了%s,卖%d元/斤" % (who,good_description,good_price)

 if good_price <= reasonable_price:
 	print '她认为便宜'
 	is_cheap = True
 	print '她买了%d斤' % (buy_amount)
 else:
 	print '她认为贵了'
 	is_cheap = False
 	print '她并没有买，扬长而去'

if __name__ == '__main__':
	main()

#作业3
#2.可以修改条件语句
def main():
 who = '艾妈妈'
 good_price = 6  #小贩的价格
 good_description = "小青菜" #小贩的招牌

 is_cheap = False #是否便宜
 reasonable_price = 5 #老妈能接受的最高价格
 buy_amount = 2 #准备买2斤


 #开始你的表演
 #go 我们来走一组
 print "%s上街看到了%s,卖%d元/斤" % (who,good_description,good_price)

 if good_price >= reasonable_price:
 	print '她认为便宜'
 	is_cheap = True
 	print '她买了%d斤' % (buy_amount)
 else:
 	print '她认为贵了'
 	is_cheap = False
 	print '她并没有买，扬长而去'

if __name__ == '__main__':
	main()



#作业4
#用自己的话解释 变量  if 和 <= >= 等符号
#变量：通过变量名储存在计算机中，并且可以对其值进行处理。
#if语句：通过对不同条件进行判断，从而实现不同的操作。
#<= >=:一般在条件语句中对条件进行判断，比较符号两边值的大小或True&False。

#作业5
#加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
def main():
 who = '艾妈妈'
 good_price = 3  #小贩的价格
 good_description = "小青菜" #小贩的招牌

 is_cheap = False #是否便宜
 reasonable_price = 5 #老妈能接受的最高价格
 buy_amount = 2 #准备买2斤


 #开始你的表演
 #go 我们来走一组
 print "%s上街看到了%s,卖%d元/斤" % (who,good_description,good_price)

 if good_price <= reasonable_price:
 	print '她认为便宜'
 	is_cheap = True
 	n = reasonable_price - good_price
 	buy_amount = buy_amount + n
 	if buy_amount <= 4:
 	    print '她买了%d斤' % (buy_amount)
 	else:
 		print '4斤就行了，多了吃不完 '
 else:
 	print '她认为贵了'
 	is_cheap = False
 	print '她并没有买，扬长而去 '

if __name__ == '__main__':
	main()
