#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Xiangwan

# For beginner
# 1. variable - num,str,bool
# 2. if
# 3. > < >= <= ==
# 4. print
def main():
	who = '向晚的老妈 '
	good_price = 4	#小贩的价格
	good_description = "西双版纳大白菜 " #小贩的招牌
	is_cheap = False #是否便宜
	reasonable_price = 5 #老妈能接受的最高价格
	buy_amount = 2 #准备买2斤

	#GO 走一组
	print "%s上街看到了%s, 卖 %d 元/斤 " % (who, good_description, good_price)

	if good_price <= reasonable_price:
	  print '她认为便宜 '
	  is_cheap = True
	  #这里开始解决老妈买几斤的问题
    	#5-2 4-3 3-4 2-4
	  buy_amount = 2 + (reasonable_price - good_price)
	  if buy_amount > 4:
	  	buy_amount = 4
	  print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去 '

	# run function
if __name__ == '__main__':
  main()

  #homework 4：
  #1.number就是数字；string就是字符串，比如中文语句；boolean就是只能赋值是与否的判断逻辑
  #2.if就像是一个条件语句，表明什么条件下执行什么命令，如果不在这个条件下就执行另一个命令
  #3.>大于 <小于 >=大于等于 <=小于等于 ==等于，在需要用到数字的时候可以用这些来帮助设置判断条件