#!/usr/bin/python
#_*_coding:utf-8 _*_
#@author: B20840

# 1. function(code block)
#	one file multiple function (code block)
# 2. return (pass variable)
# 3. return multiple variables
#
# #原则# 单一职责原则
#

def talk_with_daddy(is_cheap3,buy_amount3):
	if is_cheap3:
		print '老妈回到家里，跟老爸说："今天去买菜，价格不贵，买了 %d 斤"。' %(buy_amount3)
	else:
		print '老妈回到家里，跟老爸说："今天去买菜，菜好贵，我没买"。'

def record(record_account3): #记记记在这里
	print'老妈在小本子记了今天的买菜花销 %d 元' %(record_account3)

def buybuybuy():
	good_price = 4 #每降低一元，多买一斤
	reasonable_price =5
	buy_amount =2 #每降低一元，多买一斤

	who = '我的老妈'
	good_description = "西双版纳大白菜"

	is_cheap = False

	record_account=good_price*buy_amount

	print "%s 上街看到了 %s, 卖 %d 元/斤" %(who, good_description, good_price)

	if good_price<=reasonable_price:
		print '她认为便宜'
		is_cheap=True
		#解决老妈买几斤的问题
		#5-2 4-3 3-4 2-4 1-4
		buy_amount = 2 +(reasonable_price - good_price)
		if buy_amount>4:
			buy_amount=4
		print '她买了%d斤' %(buy_amount)
	else:
		print '她认为贵了'
		is_cheap=False
		print'她并没有买，扬长而去'

	return is_cheap, buy_amount, record_account

def  main():
	#买买买
	is_cheap2, buy_amount2, record_account2 = buybuybuy()

	#说说说
	talk_with_daddy(is_cheap2,buy_amount2)

	#记记记
	record(record_account2)

if __name__=='__main__':
	main()







