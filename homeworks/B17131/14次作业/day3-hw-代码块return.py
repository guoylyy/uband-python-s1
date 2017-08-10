#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: youngmpjlt
#day 3 新任务

#设置新的代码块
def talk_with_daddy(is_cheap3, buy_amount3):
	if is_cheap3:
		print '老妈回到家里，跟老爸说：“今天去买菜，价格不贵，买了%d斤”。' %(buy_amount3)
	else:
		print '老妈回到家里，跟老爸说：‘今天去买菜，菜好贵额，没买”。'

def mum_keep_account(is_cheap3, buy_amount3, good_price3):
	total_price=buy_amount3*good_price3
	if is_cheap3:
		print '之后，老妈回房间在账本上记下：“今天去买大白菜，价格不贵，%d元一斤，买了%d斤,共花费%d元”。' %(good_price3, buy_amount3,total_price)
	else:
		pass #print '之后，老妈回房间在账本上记下：“今天去买大白菜，菜好贵额，%d元一斤，没买”。' %(good_price3) 
		#对啊，没花费不用记账。

def buybuybuy():
	good_price = 6  #每降低一元，多买一斤
	reasonable_price = 5 
	buy_amount = 2 #每降低一元，多买一斤


	who = '片寄的老妈'
	good_description = "西双版纳大白菜" 

	is_cheap = False 

	print "%s上街看到了%s, 卖%d 元/斤" % (who, good_description, good_price)

	if good_price <= reasonable_price:
		print '她认为便宜'
		is_cheap = True
		buy_amount = 2 + (reasonable_price - good_price)
		if buy_amount > 4:
			buy_amount = 4
		print '她买了%d 斤' % (buy_amount)
	else:
		print '她认为贵了'
		is_cheap = False
		print '她并没有买，扬长而去'

    return is_cheap, buy_amount, good_price #return其实就是一个传递的作用，写在什么下面就是起什么的传递作用


def main():
  is_cheap2, buy_amount2,good_price2 = buybuybuy()
  talk_with_daddy(is_cheap2, buy_amount2)
  mum_keep_account(is_cheap2, buy_amount2,good_price2)

if __name__ == '__main__':
  main()

