#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: IPLAY

def main():
	#01. int
	apple_number = 5
	apple_price = 4.8
	pie_number = 6
	pie_price = 6.7

	#02. * /
	apple_total_price = apple_number *apple_price
	pie_total_price = pie_number *pie_price

	#03. try to explain what's float
	print "pie cost %d" % (pie_total_price) #%s表示字符串string，%d表示整数dec 十进制
	print "pie cost %g" % (pie_total_price) #%g浮点数(根据值的不同自动选择%e或%f)
	print "pie cost %e" % (pie_total_price) #%e浮点数字(科学计数法) 
	print "pie cost %0.2f" % (pie_total_price) #%f浮点数字(用小数点符号)默认6位有效数字
	print "pie cost %f" % (pie_total_price) 
	print "pie cost %.2f" % (pie_total_price)
	print "pie cost %07.2f" % (pie_total_price)
	print "pie cost %7.2f" % (pie_total_price)
	#04. **
	number = 2**3 #幂 2**3=2*2*2
	print "number = %d" % (number)

	#05. what else?
	print "test: %d" % (1 != 2) #!= 不等于，比较两个对象是否相等 1 不等于 2 成立 True
	print "test: %d" % (1 >= 2) #>=大于等于 1大于等于 2 错误 False
	print "%d" % (True)
	print "%d" % (False)
	if 1:
		print "goog"
	if 0:
		print "xxx"

	if (2 != 2):
		print "weewe we w"

if __name__ == "__main__":
	main()
