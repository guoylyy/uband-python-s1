#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: xxx

# 1. 对照锅蜀黍视频里的过程自己打一遍，自己体会一下
# 2. 解释一遍自己眼中的单一职责原则是什么？
# 3. [选做]加一个记账函数'record_account'，打印：'老妈在小本子记了买菜花销xx元'（xx要计算返回哦）

#1.function(code block)
#  one file multiple fuction(code block)
#2.return (pass variable)
#3.return multiple variables
#原则：单一职责原则
#
def record_account(buy_amount3, good_price3):
	if buy_amount3:
		print '老妈在小本子记了买菜花销 %d 元 ' % (buy_amount3 * good_price3) 
def talk_with_daddy(is_cheap3, buy_amount3):
	if is_cheap3:
		print '老妈回到家里，跟老爸说:"今天去买菜，价格不贵，买了 %d 斤"。' % (buy_amount3)
	else:
		print '老妈回到家里，跟老爸说:"今天去买菜，菜好贵啊，没买"。'
def buybuybuy():
	who = '向晚的老妈 '
	good_price = 3	#每降低一元，多买一斤
	good_description = "西双版纳大白菜 " #小贩的招牌
	is_cheap = False #是否便宜
	reasonable_price = 5 #老妈能接受的最高价格
	buy_amount = 2 #每降低一元，多买一斤
	print "%s上街看到了%s, 卖 %d 元/斤 " % (who, good_description, good_price)
	if good_price <= reasonable_price:
	  print '她认为便宜 '
	  is_cheap = True
	  #这里开始解决老妈买几斤的问题
	  buy_amount = 2 + (reasonable_price - good_price)
	  if buy_amount > 4:
	  	buy_amount = 4
	  print '她买了 %d 斤' % (buy_amount)
	else:
		print '她认为贵了 '
		is_cheap = False
		print '她并没有买，扬长而去 '
	return is_cheap, buy_amount, good_price
def main():
  is_cheap2, buy_amount2, good_price2 = buybuybuy()#买买买
  talk_with_daddy(is_cheap2, buy_amount2)#说说说
  record_account(buy_amount2, good_price2)#记记记


if __name__ == '__main__':
	main()


#我眼中的单一职责原则：每个代码块（以def为标志）只负责一件事情，
#如果重新写一个def标志的代码块，则不能在没有调用的前提下使用另一个代码块的作用。
#我们今天学的Return就是一个可以帮助我们调用代码块的语句。