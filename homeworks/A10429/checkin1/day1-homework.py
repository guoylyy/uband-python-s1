#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 1. 对照锅蜀黍的代码自己打一遍
def main():
  who = '锅蜀黍的老妈'
  good_price = 6  #小贩的价格
  good_description = "西双版纳大白菜" #小贩的招牌

  is_cheap = False #是否便宜
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤

  # 开始你的表演
  # go 我们来走一组
  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    print '她买了 %d 斤' % (buy_amount)
  else:
    print '她认为贵了'
    is_cheap = False
    print '她并没有买，扬长而去'
    
    #homework
    #1. 看 day1-homework.py

# run function
if __name__ == '__main__':
  main()
# 2. 把锅蜀黍的老板改成你老妈，跑通
def main():
	who = '那个谁的老妈'
	good_price = 6 #小贩的价格
	good_description = "西双版纳大白菜" #小贩的招牌

	is_cheap = False #是否便宜
	reasonable_price = 5 #老妈能接受的最高价格
	buy_amount = 2 #准备买2斤

	print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

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
# 3. 如果要让老妈买 2 斤大白菜而不是扬长而去，修改哪几个地方可以达到目的？（修改，并跑通）
# solution1-lower price
def main():
	who = '那个谁的老妈'
	good_price = 4.99 #小贩的价格
	good_description = "西双版纳大白菜" #小贩的招牌

	is_cheap = False #是否便宜
	reasonable_price = 5 #老妈能接受的最高价格
	buy_amount = 2 #准备买2斤

	print "%s上街看到了%s，卖 %0.2f 元/斤 " % (who, good_description, good_price)

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
# solution2-higher reasonable price
def main():
	who = '那个谁的老妈'
	good_price = 6 #小贩的价格
	good_description = "西双版纳大白菜" #小贩的招牌

	is_cheap = False #是否便宜
	reasonable_price = 6 #老妈能接受的最高价格
	buy_amount = 2 #准备买2斤

	print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

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

# 4. 做 day1-note 里面的思考题，用自己的话解释 变量  if 和 <= >= 等符号
#问1. what's the meaning of 'number', 'string', 'boolean' in python? 
#答：这些都是python中的变量，number表示数值，比如1，2，30比如2斤白菜里的2这个数字；string表示字符串，一串字符。比如“XXX的老妈”，白菜的名称“东北大白菜”；
#boolean就是布尔型数据，包括True和False等。
#问2. try to describe the meaning of 'if' statement in your mind?
#答：if条件语句，就是说，当特定条件成立（或者说if后为true）时，后面要执行指定动作，否则Else之后就执行其他动作。
#问3. Why we need > < ==  >= <= ...etc...?
#答：因为客观问题的情况不是只有1个，有时候问题比较复杂，需要根据不同情况来分别处理，比如出去吃饭，排队人数少于5桌，可以等等，那如果排队人数多于
#30桌，那性子急的人就不想等了。所以既然要解决的问题需要分情况，那么程序语言也要有相应的符号去指示它，所以有了这些><==之类的符号。

# 5. 加分题[选做]：修改程序，小贩的价格每低 1 元，老妈会多买一斤，最多买 4 斤，用程序表达出来
def main():
  who = '锅蜀黍的老妈'
  good_price = 4  #小贩的价格
  good_description = "西双版纳大白菜" #小贩的招牌

  is_cheap = False #是否便宜
  reasonable_price = 5 #老妈能接受的最高价格
  buy_amount = 2 #准备买 2 斤

  # 开始你的表演
  # go 我们来走一组
  print "%s上街看到了%s，卖 %d 元/斤" % (who, good_description, good_price)

  if good_price <= reasonable_price:
    print '她认为便宜'
    is_cheap = True
    if good_price >= 3: #reasonable_price等于5时，价格高于3块钱一斤才会改变买的斤数
      buy_amount = 2 + 5 - good_price #价格高于3块一斤时，价格每下降一块，老妈多买一斤
      print '她买了 %d 斤' % (buy_amount)
    else:
      print '她买了 4 斤'#价格低于3块一斤的情况下，老妈也只会买4斤
  else:
    print '她认为贵了 '
    is_cheap = False
    print '她并没有买，扬长而去'

if __name__ == '__main__':
  main()
  
# 6. xxx 还有两天的作业明天和后天放出来，属于阅读理解 + 练习深化
#   （ps：第 5 题错了也没关系，提交上来过后我会讲评）
def main():
  pass

if __name__ == '__main__':
  main()
