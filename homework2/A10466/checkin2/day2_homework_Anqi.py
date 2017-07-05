#!/usr/bin/python
# -*- coding: utf-8 -*-
# @author: Anqi
def main():
  #01.int 
	apple_number = 5
	apple_price = 6.3
	pie_number = 6
	pie_price = 7.2
  
  #02. *  /
	apple_total_price = apple_number * apple_price
	pie_total_price = pie_number * pie_price
  
  #03. try to explain what's float
	print 'pie cost %d ' % (pie_total_price) #取整数
	print 'pie cost %g ' % (pie_total_price) #保留1位
	print 'pie cost %0.2f ' % (pie_total_price) #保留2位

  #04. ** 次方
	number = 2**3
	print 'number = %d' % (number)

  #05. what else? 
  #    在 python简明教程中找到第 34 页，然后搞懂所有的符号～ 
  #    每个符号在下面测试一下 除了 << >> ^ ~ 几个不用理解，之后会讲
  #    不用理解优先级，只用记住一句:括号里面的最先计算
  #如:
	#print 'test: %d' % (1 != 2)
	#print 'test: %d' % (1 >= 2)
	#if 1:
		#print 'goog'
	#if 0:
		#print 'xxx'
	#if(2 != 2):
		#print 'wweewe we w'
  #请开始你的表演
 	print 2+3
 	print 4.5-3.2
 	print 3*4
 	print 5**2
 	print 4//3
 	print 4%3
 	x=3
 	y=5
 	
	if x <= y:
		print "她买了3斤"

if __name__ == '__main__':
 	main()