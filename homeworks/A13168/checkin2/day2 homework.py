#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Stephy

def main():	
	#01.int 
	apple_number = 5
	apple_price = 4.8
	pie_number = 6
	pie_price = 6.7

	x = True
	y = False

	#02. *  /
	apple_total_price = apple_number * apple_price
	pie_total_price = pie_number * pie_price
	total_price = apple_total_price + pie_total_price

	#03. try to explain what's float
	print 'pie cost %d ' % (pie_total_price)  #整数
	print 'pie cost %g ' % (pie_total_price)  #原始值，最多保留小数点后6位
	print 'pie cost %f ' % (pie_total_price)  #默认保留小数点后6位
	print 'apple cost %0.3f' % (apple_total_price)  #可指定保留几位
	print 'total cost %g ' % (total_price)

	#04. **
	number = 3 ** 4
	print 'number = %d ' % (number)

	#05. test
	print '%d ' % (8/4)
	print '%d ' % (13//3) #整除
	print '%d ' % (29%3)  #除完剩下的余数
	print '%d ' % (5&3)
	print 'true %d ' % (4<=5)
	print 'false %d ' % (3==5)

	if (5!=6):
		print 'right'
	else:
		print 'd'

	if 0 : 
		print 'yes'

	print (not y)	
	print (x and y)	
	print (x or y)		

	



		







if __name__ == '__main__':
  main()